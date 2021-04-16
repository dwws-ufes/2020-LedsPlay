from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import inlineformset_factory
from django.forms.models import modelformset_factory
from django.shortcuts import render, redirect
from django.urls.base import reverse, reverse_lazy
from django.views import generic, View
from django.forms import formset_factory

from .models import Profissional, Competencia
from .forms import ProfissionalForm, CompetenciaForm
from django.urls.base import reverse_lazy
from django.views import generic, View


class UpdateProfissionalView(LoginRequiredMixin, generic.UpdateView):
    model = Profissional
    form_class = ProfissionalForm
    template_name = "Pessoa/detail_form.html"
    success_url = reverse_lazy("dashboard")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Atualizar profissional"
        return context

    def get_object(self):
        return Profissional.objects.get(pk=self.request.user.pk)


class ProfissionalDashboardView(LoginRequiredMixin, View):
    def get(self, request):
        profissional = Profissional.objects.get(pk=request.user.pk)
        # competencias = Profissional.competencias_set.all()
        # order_count = competencias.count()

        # my_filter = CompetenciaFilter(request.GET, queryset=competencias)
        # competencias = my_filter.qs

        context = {
            "profissional": profissional,
            # "competencias": competencias,
            # "order_count": order_count,
            # "myFilter": my_filter,
        }
        return render(request, "Dashboard/userdashboard.html", context)

class CreateCompetenciaView(LoginRequiredMixin, View):
    CompetenciaFormSet = modelformset_factory(Competencia, CompetenciaForm, extra=5)
    profissional = None

    def get(self, request):
        self.profissional = Profissional.objects.get(pk=request.user.pk)
        formset = self.CompetenciaFormSet(queryset=Competencia.objects.none())
        context = {"formset": formset}
        return render(request, "Dashboard/form.html", context)


    def post(self, request):
        self.profissional = Profissional.objects.get(pk=request.user.pk)
        formset = self.CompetenciaFormSet(request.POST)
        if formset.is_valid():
            objs = formset.save()
            for obj in objs:
                self.profissional.competencias.add(obj)
            return redirect("professional:dashboard")
        context = {"formset": formset}
        return render(request, "Dashboard/form.html", context)


class UpdateCompetenciaView(generic.UpdateView):
    model = Competencia
    form_class = CompetenciaForm
    template_name = "Dashboard/form.html"
    success_url = reverse_lazy("dashboard")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Atualizar competência"
        return context

class DeleteCompetenciaView(generic.DeleteView):
    model = Competencia
    template_name = "Dashboard/delete.html"
    success_url = reverse_lazy("dashboard")
