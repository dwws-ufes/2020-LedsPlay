from .models import Cliente
from register.forms import PessoaForm


class ClienteForm(PessoaForm):
    class Meta:
        model = Cliente
        fields = ["nome", "sexo", "nascimento", "cidade", "interesse"]