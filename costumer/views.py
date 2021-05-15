from .models import Cliente, Ordem
from django.contrib.auth.models import User
from register.models import Pessoa
from .forms import ClienteForm
from django.urls.base import reverse, reverse_lazy
from django.views import generic, View
from django.forms import inlineformset_factory
from django.views import generic
from .filters import OrdemFilter
from .forms import OrdemForm
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
# from django.models import Profissional
from professional.models import Profissional
from rdflib.namespace import Graph, Namespace, URIRef, BNode, Literal, CSVW, DC, DCAT, DCTERMS, DOAP, FOAF, ODRL2, ORG, OWL, \
                           PROF, PROV, RDF, RDFS, SDO, SH, SKOS, SOSA, SSN, TIME, \
                           VOID, XMLNS, XSD


class UpdateClienteView(LoginRequiredMixin, generic.UpdateView):
    model = Cliente
    form_class = ClienteForm
    template_name = "Pessoa/detail_form.html"
    success_url = reverse_lazy("costumer:dashboard")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Atualizar usuário"
        return context

    def get_object(self):
        return Cliente.objects.get(pk=self.request.user.pk)


class CostumerDashboardView(LoginRequiredMixin, View):
    def get(self, request):
        cliente = Cliente.objects.get(pk=request.user.pk)
        ordens = cliente.ordem_set.all()

        my_filter = OrdemFilter(request.GET, queryset=ordens)
        ordens = my_filter.qs
        nOrdens = ordens.count()

        context = {
            "cliente": cliente,
            "ordens": ordens,
            "nOrdens": nOrdens,
            "myFilter": my_filter,
        }
        return render(request, "Dashboard/userdashboard.html", context)


class CreateOrderView(LoginRequiredMixin, View):
    OrderFormSet = inlineformset_factory(Cliente, Ordem, OrdemForm, extra=5)
    customer = None

    def get(self, request):
        self.customer = Cliente.objects.get(pk=request.user.pk)
        formset = self.OrderFormSet(
            queryset=Ordem.objects.none(), instance=self.customer
        )
        context = {"formset": formset}
        return render(request, "Dashboard/form.html", context)

    def post(self, request):
        self.customer = Cliente.objects.get(pk=request.user.pk)
        formset = self.OrderFormSet(request.POST, instance=self.customer)
        if formset.is_valid():
            formset.save()
            return redirect("costumer:dashboard")
        context = {"formset": formset}
        return render(request, "Dashboard/form.html", context)


class ExportProfessionalsView(LoginRequiredMixin, View):
    # OrderFormSet = inlineformset_factory(Cliente, Ordem, OrdemForm, extra=5)
    # customer = None

    def get(self, request):
        g = Graph()
        g.bind("foaf", FOAF)

        n = Namespace("http://example.org/people/")

        n.bob  # = rdflib.term.URIRef(u'http://example.org/people/bob')
        n.eve  # = rdflib.term.URIRef(u'http://example.org/people/eve')

        bob = URIRef("http://example.org/people/Bob")
        linda = BNode()  # a GUID is generated

        name = Literal('Bob')  # passing a string
        age = Literal(24)  # passing a python int
        height = Literal(76.5)  # passing a python float

        g.add((bob, RDF.type, FOAF.Person))
        g.add((bob, FOAF.name, name))
        g.add((bob, FOAF.knows, linda))
        g.add((linda, RDF.type, FOAF.Person))
        g.add((linda, FOAF.name, Literal("Linda")))
        profissionais = Profissional.objects.all()
        print(profissionais)
        print(FOAF.knows)
        # self.customer = Cliente.objects.get(pk=request.user.pk)
        # formset = self.OrderFormSet(
        #     queryset=Ordem.objects.none(), instance=self.customer
        # )
        # context = {"formset": formset}
        print(g.serialize(format="turtle").decode("utf-8"))
        
        return "Hello, World"


class UpdateOrdemView(LoginRequiredMixin, generic.UpdateView):
    model = Ordem
    form_class = OrdemForm
    template_name = "Dashboard/form.html"
    success_url = reverse_lazy("costumer:dashboard")

    def get_object(self, **kwargs):
        ordem_pk = self.kwargs.get(self.pk_url_kwarg)
        ordem = Ordem.objects.get(pk=ordem_pk)
        cliente = Cliente.objects.get(pk=self.request.user.pk)
        # Cliente só edita as ordens dele
        if cliente == ordem.nome:
            return ordem
        return None


class DeleteOrdemView(LoginRequiredMixin, generic.DeleteView):
    model = Ordem
    template_name = "Dashboard/delete.html"
    success_url = reverse_lazy("costumer:dashboard")

    def get_object(self):
        ordem_pk = self.kwargs.get(self.pk_url_kwarg)
        cliente = Cliente.objects.get(pk=self.request.user.pk)
        ordem = Ordem.objects.get(pk=ordem_pk)
        # Cliente só deleta as ordens dele
        if cliente == ordem.nome:
            return ordem
        return None
