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
# instructor planta e instructor por contrat

from modules import classes as classes# Importo modulo clases donde esta la informacion principal del programa 
from modules import menu
from random import randint # Importo randint para sacar valore aleatorios en algunos estados 
from datetime import datetime, timedelta # Importo esta libreria para sincronia y controles con la fecha DD-MM-AA
from colorama import Fore,Back # Importo colorama para color fondo y fuente


def main(): # Este el programa pricipal de app 

  print(Fore.BLACK + Back.BLUE)# Defino colores fondo y fuente 

  if __name__ == "__main__": # Declaracion que me indica que este es el modulo principal del programa 
    main()

