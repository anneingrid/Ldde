import Ldde


lista = Ldde.Ldde()


# lista.inserir_inicio('C')
# lista.inserir_inicio('B')
# lista.inserir_inicio('A')
# lista.inserirAposDet('D','E')
# lista.inserirAposDet('x','A')
# lista.inserir_inicio('z')
# lista.show()


lista.inserir_inicio('C')
lista.inserir_inicio('B')
lista.inserir_inicio('A')
lista.inserirAposDet('D','C')
lista.inserir_fim('E')
lista.show()
lista.inserirAposDet('F','A')
lista.show()
lista.remover('A')
lista.show()
lista.remover('K')
lista.show()