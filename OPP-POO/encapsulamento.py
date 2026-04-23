#ENCAPSULAMENTO
#Nas linguagens clássicas, terão métodos e atributos public, protected, private

class BaseDeDados: #não é uma base de dados (nem um bom nome para uma), porém é um dicionário que iremos tratar como uma base de dados
    def __init__(self):
        self.dados = {} #[...]isso ta dentro

def inserir_clientes(self, id, nome):
    if 'clientes' not in self.dados:
        self.dados['clientes'] = {id: nome}
    else:
        self.dados['clientes'].update({id: nome})

def lista_clientes(self):
    for id, nome in self.dados['clientes'].items():
        print(id, nome)

def apaga_clientes(self, id):
    del self.dados['clientes'][id]

bd = BaseDeDados() #[...] e também fora da base de dados, lido como público, pois em python não temos um método exato para isso e esse é o mais equivalente
bd.inserir_cliente(1, 'Otavio')
bd.inserir_cliente(2, 'Miranda')
bd.inserir_cliente(3, 'Rose')
bd.apaga_cliente(2)
bd.lista_clientes()

#13:06