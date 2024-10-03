class Televisao:
 
    def __init__(self): # método construtor
        self.__canal = 1    # atributo privado
        self.__volume = 0   # atributo privado
 
    def aumentar_volume(self):
        volume = self.__volume + 1
        self.__volume = volume if volume <= 10 else 10
        self.__imprimir()
 
    def diminuir_volume(self):
        volume = self.__volume - 1
        self.__volume = volume if volume >= 0 else 0
        self.__imprimir()
 
    def trocar_canal(self, canal):
        if 1 <= canal <= 15:
            self.__canal = canal
        else:
            self.__canal = 1
        self.__imprimir()
 
    def __imprimir(self):   # método privado
        print("Televisão")
        print("Volume:", self.__volume, "- Canal:", self.__canal)
 
 
if __name__ == '__main__':
    televisao = Televisao()
    televisao.trocar_canal(5)
    televisao.aumentar_volume()
    televisao.aumentar_volume()
    televisao.trocar_canal(20)
    televisao.diminuir_volume()   