#POO py.

#Declaração de Classe
class JovensPS:
    def __init__(self): # Método Construtor
        #Atributos de Instância
        #self é um nome genérico de um atributo de instância
        self.nome = " "
        self.idade = 0
    
    #Métodos de Instância
    def aniversario(self):
        self.idade = self.idade + 1 #somando mais um
        #ou self.idade += 1

    def mensagem(self):
        return f"{self.nome} é um Jovem e tem {self.idade} anos de idade."

#Declaração de Objetos
g1 = JovensPS()
g1.nome = "Maria"
g1.idade = 17
g1.aniversario()
print(g1.mensagem())

g2 =JovensPS()
g2.nome = "Mauro"
g2.idade = 53
print(g2.mensagem())

#g1 é um objeto e JovensPS é minha classe
#entre parenteses chama meu método construtor
