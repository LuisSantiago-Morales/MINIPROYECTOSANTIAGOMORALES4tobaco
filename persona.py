class persona():
    def init(self, numero, nombre, direccion):
        self.nombre = nombre
        self.numero= numero
        self.direccion = direccion

        #CREACION DE GETTERS
        def verNombre(self):
            return self.nombre
        def verNumero(self):
            return self.numero 
        def verDireccion(self):
            return self.direccion

        #CREACION DE SETTERS
        def modificarNombre(self, nuevoNombre):
            self.numero = nuevoNombre
        def modificarNumero(self, nuevoNumero):
            self.numero = nuevoNumero  
        def modificarDireccion(self, nuevaDireccion):
           self.numero = nuevaDireccion                                        