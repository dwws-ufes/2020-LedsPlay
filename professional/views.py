from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Profissional
from .forms import ProfissionalForm
from django.urls.base import reverse_lazy
from django.views import generic


class UpdateProfissionalView(generic.UpdateView):
    model = Profissional
    form_class = ProfissionalForm
    template_name = "Pessoa/detail_form.html"
    success_url = reverse_lazy("dashboard")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Atualizar usuário"
        return context

    def get_object(self):
        return Profissional.objects.get(pk=self.request.user.pk)
