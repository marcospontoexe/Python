class Jedi:
    def __init__(self, name):  # método construtor
        self.jedi_name = name  

    def say_hi(self):
        print('Hello, my name is ', self.jedi_name)

'''
Caso essa classe seja executada, sem instanciar um objeto por exemplo,
será executada a condição a baixo.
'''
if __name__ == '__main__':

    j1 = Jedi('ObiWan') # instancia um objeto   
    j1.say_hi()         # executa um método do objeto

    j2 = Jedi('Anakin')
    j2.say_hi()