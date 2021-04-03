from .models import Cliente
from .forms import ClienteForm
from django.urls.base import reverse_lazy
from django.views import generic

class UpdateClienteView(generic.UpdateView):
    model = Cliente
    form_class = ClienteForm
    template_name = "Pessoa/detail_form.html"
    success_url = reverse_lazy("register:cadastrados") # TODO: Redirecionar pra dashboard do Cliente

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = "Atualizar usuário"
        return context

    def get_object(self):
        return Cliente.objects.get(pk=self.request.user.pk)
