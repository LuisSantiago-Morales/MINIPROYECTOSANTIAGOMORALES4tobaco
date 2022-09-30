class persona:
     def __init__(self,nombre,numero,direccion):
         self.__nombre=nombre
         self.__numero=numero
         self.__direccion=direccion

        #CREACION DE GETTERS
     def verNombre(self):
         return self.__nombre

     def verNumero(self):
         return self.__numero
     def verDireccion(self):
         return self.__direccion

        #CREACION DE SETTERS
     def modificarnombre(self, nuevonombre):
        self.__nombre = nuevonombre   
     def modificarnumero(self, nuevonumero):
        self.__numero = nuevonumero
     def modificardireccion(self, nuevadireccion):
        self.__direccion = nuevadireccion                                  