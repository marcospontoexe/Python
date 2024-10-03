class Jedi:
    # método construtor
    def __init__(self, name):  # self é usado para referenciar ao construtor do objeto que chamou a classe
        self.jedi_name = name  

    def say_hi(self):
        print('Hello, my name is ', self.jedi_name)

'''
As linhas dentro do bloco if __name__ == '__main__': só serão executadas caso o arquivo Classe.py seja executado diretamente. 
Caso seja feita sua importação, esses códigos não serão executados.
'''
if __name__ == '__main__':

    j1 = Jedi('ObiWan') # instancia um objeto   
    j1.say_hi()         # executa um método do objeto

    j2 = Jedi('Anakin')
    j2.say_hi()
