from persona import persona 
misContactos = []

def crearContacto(nombre, numero, direccion):
  misContactos.append(persona(nombre, numero, direccion))
  print("Contacto almacenado...")

def buscarContacto(nombre):
  if len(misContactos) == 0:
    print("La lista está vacia, no hay contactos...")
  else:
    encontrado = False
    for i in range(len(misContactos)):
     if misContactos[i].verNombre() == nombre:  
       print("El telefono es: ", misContactos[i].verNumero())
       print("La direccion es:", misContactos[i].verDireccion())
       encontrado=True
       break
     else:
       encontrado = False
    if encontrado == False:
      print("Dato no existente...")             

def mostrarContacto():
  if len(misContactos)  == 0:
    print("La lista está vacia, no hay contactos para buscar...")
  else:
    for i in range (len(misContactos)):
      print('Nombre:',misContactos[i].verNombre(),'Direccion: ',misContactos[i].verDireccion(), 'telefono: ',misContactos[i].verNumero())

def modificarContacto(nombre):
  if len(misContactos) == 0:
    print("La lista está vacia, no hay contactos...")
  else:
    encontrado = False
    posicion = None 
    for i in range(len(misContactos)):
      if misContactos[i].verNombre()==nombre:
          posicion = i   
          encontrado = True
          break
    else:
         encontrado = False
    if encontrado:
      nuevoNombre = input("Ingrese el nuevo nombre: ")
      nuevoNumero = int(input("Ingrese el nuevo número: "))
      nuevaDireccion = input("Ingrese la nueva direccion: ")
      misContactos[posicion].modificarnombre(nuevoNombre)
      misContactos[posicion].modificarnumero(nuevoNumero)
      misContactos[posicion].modificardireccion(nuevaDireccion)
      print("Datos actualizados con exito...")
    else:
       print("Dato no encontrado...") 

def eliminarContacto(nombre):
    if len(misContactos) == 0:
      print("La lista está vacia, no hay contactos...")
    else:
      encontrado = False
      posicion = None 
      for i in range(len(misContactos)):
        if misContactos[i].verNombre() == nombre:
          posicion = i   
          encontrado = True
          break
        else:
          encontrado = False
      if encontrado:
        misContactos.pop(posicion)
        print("Dato eliminado con exito...")
      else:
        print("Dato no encontrado...") 

def crearReporte():
    documento = open("reporte.html","w")
    documento.write("<!doctype html>\n")
    documento.write("<html>\n")
    documento.write("<head>\n")
    documento.write("\t<title>Agenda 2022</title>\n")
    documento.write("</head>\n")
    documento.write("<body>\n")
    documento.write("\t<center>\n")
    documento.write("\t<h1>Mis Contactos</h1>\n")
    documento.write('\t<table border ="1">\n')
    documento.write("\t\t<tr>\n")
    documento.write("\t\t\t<td>Numero de telefono</td><td>Nombre</td><td>Dirección</td>\n")
    for i in range(len(misContactos)):
       documento.write("\t\t<tr>\n")
       documento.write("\t\t\t<td>" + misContactos[i].verNombre()+ "</td><td>" + str(misContactos[i].verNumero()) + "</td><td>" + misContactos[i].verDireccion() + "</td>")
       documento.write("</tr>\n")

    documento.write("\t\t</tr>\n")
    documento.write("\t\t</table>\n")
    documento.write("\t</center>\n")
    documento.write("</body>\n")
    documento.write("</html>")
    documento.close()
    print("Reporte HTML creado con éxito...")
               
def main():
  op = 0
  while op != 7:
      print("---------------------AGENDA TELEFONICA---------------")
      print("1. Crear contacto")
      print("2. Buscar contacto")
      print("3. Ver contactos")
      print("4. Modificar contacto")
      print("5. Eliminar contacto")
      print("6. Crear reporte en HTML")
      print("7. Salir del programa \n\n")
      op= int(input("Ingrese el número de opción: "))
      if op ==1:
       nombre  = (input("Ingrese su nombre: "))
       numero = int(input("Ingrese su numero: "))
       direccion = (input("Ingrese su direccion: "))
       crearContacto(nombre, numero, direccion)

      elif op == 2:
       nombre = input("Ingrese el nombre del contacto a buscar: ")
       buscarContacto(nombre)

      elif op ==3:
       mostrarContacto()
       
      elif op ==4:
       nombre = input("Ingrese el nombre del contacto:")
       modificarContacto(nombre) 

      elif op == 5:
       nombre = input("Ingrese el nombre del contacto:")
       eliminarContacto(nombre)
      
      elif op==6:
         crearReporte()
      
      elif op==7:
        print('-----------------SALIENDO DEL PROGRAMA-------------------')

    #INICIAR PROGRAMA
  

main()