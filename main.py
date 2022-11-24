from NYPizzaStore import NYPizzaStore
from NYStyleCheesePizza import NYStyleCheesePizza


nyStore = NYPizzaStore()

pizza = nyStore.orderPizza('cheese')

print('Kto-to zakazal', pizza.getName())

               
