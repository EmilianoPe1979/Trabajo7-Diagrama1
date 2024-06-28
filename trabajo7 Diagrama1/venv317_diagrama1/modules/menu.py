#***************************************#
# CENTRO DE BIOTECNOLOGIA AGROPECUARIA  #
# NOMBRE EMILIANO PERILLA AGUILAR       #
# VERSION : 4.0                         #
# Fecha: 09/06/2024                     #
#***************************************#

#Este programa se encuentra diseñado par demostrar la funcionalidad que resulta 
# del correcto manejo del POP, mediante super clases, subclases y clases logramos
# crear y modificar los atributos y metodos de un objeto. Super clase persona, 
# subclases Aprendiz e Instructor y clases aprendiz lectiva, aprendiz practica
# instructor planta e instructor por contrato.

from modules import classes as classes# Importo modulo clases donde esta la informacion principal del programa 
from random import randint # Importo randint para sacar valore aleatorios en algunos estados 
from datetime import datetime, timedelta # Importo esta libreria para sincronia y controles con la fecha DD-MM-AA
fecha = datetime
n_meses = int
from colorama import Fore,Back # Importo colorama para color fondo y fuente
print(Fore.BLACK + Back.BLUE)# Defino colores fondo y fuente 

while True:
  print("-----------------------")# Menu de control para hacer mas organizada la presentacion del programa 
  print("DIAGRAMA DE CLASES:")
  print("1. Datos Aprendiz Etapa Lectiva") #Opcion 1 datos del aprendiz E.L
  print("2. Datos Aprendiz Etapa Productiva")#Opcion 1 datos del aprendiz E.P
  print("3. Datos Instructor Planta") # Datos del Instructor de planta 
  print("4. Datos Instructor Contrato") # Datos del instructor de contrato 
  print("5. Salir") # Opcion 5 para salir del progrma 
  print("-----------------------")
  
  while True:
      try:
          opcion = int(input("Escoge una opción: "))
          break  # Salimos del bucle si se ingresa un número válido
      except ValueError:
          print("Opción inválida. Inténtalo nuevamente.")
    # opcion = int(input("Escoge una opcion: ")) # El usuario escoge una opcion 

  if opcion == 1:
    aprendiz2 = classes.EtapaLectiva ("", "", 0, "", 0, 0, 0) # Defino aprendiz2 como objeto de sub clase aprenziz 

    aprendiz2.leer_datos() # Esta funcion de aprendiz2 me recibe todos los datos ingresados por el usuario 

    aprendiz2.informacion_aprendiz() # Esta funcion de aprendiz2 imprime lo que se almacena en la funcion leer datos. 

    aprendiz2.estado() # Esta funcion indica el estado del aprendiz (induccion/formacion/aplazado/retirado)

  elif opcion== 2:
    aprendiz3 = classes.EtapaPractica ("", "", 0, "", "", 0, 0) # Defino aprendiz3 como objeto de sub clase aprenziz 

    aprendiz3.leer_datos() # Esta funcion de aprendiz2 me recibe todos los datos ingresados por el usuario 

    aprendiz3.informacion_aprendiz() # Esta fuuncion imprime lo que se almacena en la funcion leer datos. 

    aprendiz3.estado() # Esta funcion indica el estado del aprendiz (induccion/formacion/aplazado/retirado)


  elif opcion== 3:
    instructor1 = classes.InstructorPlanta ("", "", "", 0, 0, "")  # Defino instructor1 como objeto de sub clase instructor

    instructor1.leer_datos() # Esta funcion de aprendiz2 me recibe todos los datos ingresados por el usuario 

    instructor1.estado() # En esta funcion se imprime el estado instructor planta 

    instructor1.informacion_instructor_planta() # Esta  imprime lo que se almacena en la funcion leer datos.

    instructor1.estado()  # Esta funcion indica el estado instructor planta (Formacion/Vacaciones/licencia/Prepensionado)

    instructor1.contrato() # Esta fucion indica el contrato del instructor planta (activo/inactivo)

    instructor1.sueldo() # Esta funcion mediante operacion matematica tabula el sueldo del instructor de planta 

  elif opcion== 4:
    instructor2 = classes.InstructorContrato ("", "", "", 0, 0, "") # Defino instructor2 como objeto de sub clase instructor

    instructor2.leer_datos() # Esta funcion de aprendiz2 me recibe todos los datos ingresados por el usuario 

    instructor2.estado() # Esta funcion indica el estado instructor planta (Formacion/Vacaciones/licencia/Prepensionado)

    instructor2.informacion_instructor_contrato() # En esta funcion se  imprime lo que se almacena en la funcion leer datos.
    
    instructor2.finalizacion_contrato()
    # instructor2.sumar_meses(fecha, n_meses) # Con esta funcion 
    
    # instructor2.tiempo_contrato()

  elif opcion== 5:
    print("Adios") # Al digitar tecla 5 el usuario sale del programa y aparece el letrero 
    break # Declaracion para la finalizacion del bucle while del menu 
  else:
    print("Opcion no valida") # Si se llegase a digitar un numero diferente de 1 a 5 aparece opcion no valida 

