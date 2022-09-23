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
     def modificarNombre(self, nuevoNombre):
         self.__nombre = nuevoNombre
     def modificarNumero(self, nuevoNumero):
         self.__numero = nuevoNumero  
     def modificarDireccion(self, nuevaDireccion):
         self.__direccion = nuevaDireccion                                        