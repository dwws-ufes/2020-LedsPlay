from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import inlineformset_factory
from django.shortcuts import render, redirect
from django.urls.base import reverse, reverse_lazy
from django.views import generic, View

from .forms import ProfissionalForm
from .models import Profissional, Competencia


class UpdateProfissionalView(LoginRequiredMixin, generic.UpdateView):
    model = Profissional
    form_class = ProfissionalForm
    template_name = "Pessoa/detail_form.html"
    success_url = reverse_lazy("costumer:dashboard")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Atualizar usuário"
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

#TODO FAZER ISSO AQUI FUNCIONAR

# class CreateCompetenciaView(LoginRequiredMixin, View):
#     CompenteciaFormSet = inlineformset_factory(
#         Profissional,
#         Competencia,
#         fields=("competencia", "status"),
#         extra=5
#     )
#     profissional = None
#
#     def get(self, request):
#         self.profissional = Profissional.objects.get(pk=request.user.pk)
#         formset = self.CompenteciaFormSet(
#             queryset=Profissional.objects.none(), instance=self.profissional
#         )
#         context = {"formset": formset}
#         return render(request, "Dashboard/form.html", context)
#
#     def post(self, request):
#         self.profissional = Profissional.objects.get(pk=request.user.pk)
#         formset = self.CompenteciaFormSet(request.POST, instance=self.profissional)
#         print(formset.is_valid())
#         if formset.is_valid():
#             formset.save()
#             return redirect(reverse("professional:dashboard"))
#         context = {"formset": formset}
#         return render(request, "Dashboard/form.html", context)

