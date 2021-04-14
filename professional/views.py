from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Profissional, Competencia
from .forms import ProfissionalForm, CompetenciaForm
from django.urls.base import reverse_lazy
from django.views import generic, View


class UpdateProfissionalView(generic.UpdateView):
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


# ???
class UpdateCompetenciaView(generic.UpdateView):
    model = Competencia
    form_class = CompetenciaForm
    template_name = "Dashboard/form.html"
    success_url = reverse_lazy("dashboard")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Atualizar competência"
        return context

    def get_object(self):
        return Competence.objects.get(pk=self.request.user.pk)


class DeleteCompetenciaView(generic.DeleteView):
    model = Competencia
    template_name = "Dashboard/delete.html"
    success_url = reverse_lazy("competencia:dashboard")

    def get_object(self):
        competencia = Competencia.objects.get(pk=self.request.user.pk)


class CreateCompetenciaView(generic.CreateView):
    def get(self, request):
        self.Competencia = Competencia.objects.get(pk=request.user.pk)
        return render(request, "Dashboard/form.html", context)

    def post(self, request):
        self.Competencia = Competencia.objects.get(pk=request.user.pk)
        return render(request, "Dashboard/form.html", context)
