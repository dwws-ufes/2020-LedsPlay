from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import inlineformset_factory
from django.shortcuts import render, redirect
from django.urls.base import reverse, reverse_lazy
from django.views import generic, View

from .models import Professional, Competence
from .forms import ProfessionalForm, CompetenceForm
from django.urls.base import reverse_lazy
from django.views import generic, View


class UpdateProfessionalView(LoginRequiredMixin, generic.UpdateView):
    model = Professional
    form_class = ProfessionalForm
    template_name = "Person/detail_form.html"
    success_url = reverse_lazy("dashboard")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Atualizar professional"
        return context

    def get_object(self):
        return Professional.objects.get(pk=self.request.user.pk)


class ProfessionalDashboardView(LoginRequiredMixin, View):
    def get(self, request):
        professional = Professional.objects.get(pk=request.user.pk)
        # competences = Professional.competences_set.all()
        # order_count = competences.count()

        # my_filter = CompetenceFilter(request.GET, queryset=competences)
        # competences = my_filter.qs

        context = {
            "professional": professional,
            # "competences": competences,
            # "order_count": order_count,
            # "myFilter": my_filter,
        }
        return render(request, "Dashboard/userdashboard.html", context)

#TODO FAZER ISSO AQUI FUNCIONAR

# class CreateCompetenceView(LoginRequiredMixin, View):
#     CompenteciaFormSet = inlineformset_factory(
#         Professional,
#         Competence,
#         fields=("competence", "status"),
#         extra=5
#     )
#     professional = None
#
#     def get(self, request):
#         self.professional = Professional.objects.get(pk=request.user.pk)
#         formset = self.CompenteciaFormSet(
#             queryset=Professional.objects.none(), instance=self.professional
#         )
#         context = {"formset": formset}
#         return render(request, "Dashboard/form.html", context)
#
#     def post(self, request):
#         self.professional = Professional.objects.get(pk=request.user.pk)
#         formset = self.CompenteciaFormSet(request.POST, instance=self.professional)
#         print(formset.is_valid())
#         if formset.is_valid():
#             formset.save()
#             return redirect(reverse("professional:dashboard"))
#         context = {"formset": formset}
#         return render(request, "Dashboard/form.html", context)

# ???
class UpdateCompetenceView(generic.UpdateView):
    model = Competence
    form_class = CompetenceForm
    template_name = "Dashboard/form.html"
    success_url = reverse_lazy("dashboard")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Atualizar competência"
        return context

    def get_object(self):
        return Competence.objects.get(pk=self.request.user.pk)


class DeleteCompetenceView(generic.DeleteView):
    model = Competence
    template_name = "Dashboard/delete.html"
    success_url = reverse_lazy("dashboard")

    def get_object(self):
        competence = Competence.objects.get(pk=self.request.user.pk)


class CreateCompetenceView(generic.CreateView):
    def get(self, request):
        self.Competence = Competence.objects.get(pk=request.user.pk)
        return render(request, "Dashboard/form.html", context)

    def post(self, request):
        self.Competence = Competence.objects.get(pk=request.user.pk)
        return render(request, "Dashboard/form.html", context)
