from .models import Cliente, Ordem
from django.http import HttpResponse
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
from rdflib import Graph, Namespace, URIRef, BNode, Literal
from rdflib.namespace import CSVW, DC, DCAT, DCTERMS, DOAP, FOAF, ODRL2, ORG, OWL, \
                           PROF, PROV, RDF, RDFS, SDO, SH, SKOS, SOSA, SSN, TIME, \
                           VOID, XMLNS, XSD
from urllib.parse import urlencode, quote_plus


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
        # Define namespace para publicação de dados
        LEDS = Namespace("http://leds.leds/1/")

        ledsGraph = Graph()

        # Adiciona prefixos ao grafo
        ledsGraph.bind("leds", LEDS)
        ledsGraph.bind("foaf", FOAF)

        # Obtém dados de todos os profissionais
        profissionais = Profissional.objects.all()
        for profissional in profissionais:
            # Cria nó para profissional e cidade do profissional
            profissionalNode = URIRef(f"http://leds.leds/1/professionals/{profissional.user}")
            profissionalCityNode = URIRef(f"http://leds.leds/1/city/{profissional.cidade}")
            # print(f"Profissional: '{profissional.nome}' | média: {profissional.media or 0}, morando em {profissional.cidade}.")
            # print("- Competências:")

            # Adiciona informações ao grafo
            ledsGraph.add((profissionalNode, RDFS.subClassOf, FOAF.Person))
            ledsGraph.add((profissionalNode, RDF.type, LEDS.Professional))
            ledsGraph.add((profissionalNode, LEDS.livesIn, profissionalCityNode))
            ledsGraph.add((profissionalNode, FOAF.name, Literal(profissional.nome)))

            for competencia in profissional.competencias.all():
                # Prepara nome da competência para criar URI
                competenciaURLEncoded = quote_plus(str(competencia))
                competenceNode = URIRef(f"http://leds.leds/1/competences/{competenciaURLEncoded}")
                ledsGraph.add((profissionalNode, FOAF.knows, competenceNode))
                # print("\t", competencia)
        print(ledsGraph.serialize(format="turtle").decode("utf-8"))

        return HttpResponse(str(ledsGraph.serialize(format="turtle").decode("utf-8")), content_type="text/rdf+xml")

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
