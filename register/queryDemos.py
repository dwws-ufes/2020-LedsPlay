#***(1)Retorna todos os Usuários do DB
customers = Pessoa.objects.all()

#(2)Retorna primeiro usuário do DB
firstCustomer = Pessoa.objects.first()

#(3)Retorna ultimo usuário do DB
lastCustomer = Pessoa.objects.last()

#(4)Retorna usuário pelo nome
customerByName = Pessoa.objects.get(name='Aleph')

#***(5)Retorna usuário por ID
customerById = Pessoa.objects.get(id=4)

#***(6)Retorna todas as ordens baseado no >Primeiro Usuário
firstCustomer.order_set.all()

#(7)***Returns orders customer name: (Query parent model values)
order = Ordem.objects.first()
parentName = order.customer.name

#(8)***Retorna Competencia de acordo com Categoria
products = Competencia.objects.filter(category="A Distancia")

#(9)***Lista de Ordens Ordenadas
leastToGreatest = Competencia.objects.all().order_by('id')
greatestToLeast = Competencia.objects.all().order_by('-id')


#(10) Returns all products with tag of "Sports": (Query Many to Many Fields)
productsFiltered = Competencia.objects.filter(tags__name="Sports")

'''
(11)Bonus
Q: If the customer has more than 1 ball, how would you reflect it in the database?
A: Because there are many different products and this value changes constantly you would most 
likly not want to store the value in the database but rather just make this a function we can run
each time we load the customers profile
'''

#Returns the total count for number of time a "Ball" was ordered by the first customer
ballOrders = firstCustomer.order_set.filter(product__name="Ball").count()

#Returns total count for each product orderd
allOrders = {}

for order in firstCustomer.order_set.all():
	if order.product.name in allOrders:
		allOrders[order.product.name] += 1
	else:
		allOrders[order.product.name] = 1

#Returns: allOrders: {'Ball': 2, 'BBQ Grill': 1}


#RELATED SET EXAMPLE
class ParentModel(models.Model):
	name = models.CharField(max_length=200, null=True)

class ChildModel(models.Model):
	parent = models.ForeignKey(Customer)
	name = models.CharField(max_length=200, null=True)

parent = ParentModel.objects.first()
#Returns all child models related to parent
parent.childmodel_set.all()