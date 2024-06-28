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

from random import randint # Importo randint para sacar valore aleatorios en algunos estados 
from datetime import datetime, timedelta # Importo esta libreria para sincronia y controles con la fecha DD-MM-AA


#----------------------PERSONA--------------------------------------
class Persona: # Definicion de la superclase 


    def __init__(self, documento,nombre_completo): # Definicion de la superclase 
        self.__documento = documento   # Definicion self de los argumentos             
        self.__nombre_completo = nombre_completo      
       

    def set_documento(self, value): # Funcion que define el set del argumento documento
        self.__documento = value
    

    def get_documento(self):  # Funcion que define el get del argumento documento      
        return self.__documento
    

    def set_nombre_completo(self, value): # Define el set del argumento nombre_completo
        self.__nombre_completo = value


    def get_nombre_completo(self):  # Define el get del argumento nombre_completo
        return self.__nombre_completo

    
#----------------------APRENDIZ--------------------------------------

class Aprendiz (Persona): # Definicion de la subclase 


    def __init__(self, documento ="", nombre_completo ="", ficha = "", programa = "" ):
    #Creacion del constructor y sus argumentos 

        super ().__init__ (documento, nombre_completo)
        # Definicion de los self de los argumentos que hereda de la super clase persona
        self.__ficha = ficha    
        self.__programa = programa # Definicion self de los argumentos nuevos
        
   
    def set_ficha(self, value):  # Define el set del argumento de ficha  
        self.__ficha = value


    def get_ficha(self):        # Define el get del argumento de ficha 
        return self.__ficha


    def set_programa(self, value):  # Define el set del argumento de programa
        self.__programa = value


    def get_programa(self):      # Define el get del argumento de programa
        return self.__programa


#----------------------ETAPA LECTIVA -------------------------------------

class EtapaLectiva (Aprendiz): # Definicion de la clase 

    def __init__(self, documento = "", nombre_completo = "", ficha = 0, programa = "", numero_trimestre = 0, fecha_inicio=datetime, fecha_terminacion=datetime):
    #Creacion del constructor y sus argumentos 

        super ().__init__ (documento, nombre_completo,ficha, programa)
        # Definicion de los self de los argumentos que hereda de la subclase aprendiz

        self.__numero_trimestre = numero_trimestre
        self.__fecha_inicio = fecha_inicio  # Definicion self de los argumentos nuevos
        self.__fecha_terminacion = fecha_terminacion
   

    def set_numero_trimestre(self, value): # Define el set del argumento numero_trimestre 
        self.__numero_trimestre = value


    def get_numero_trimestre(self): # Define el get del argumento numero_trimestre
        return self.__numero_trimestre
    

    def set_fecha_inicio(self, value):  # Define el set del argumento fecha_inicio
        self.__fecha_inicio = value


    def get_fecha_inicio(self):  # Define el get del argumento fecha_inicio
        return self.__fecha_inicio


    def set_fecha_terminacion(self, value):  # Define el set del argumento fecha_terminacion
        self.__fecha_terminacion = value


    def get_fecha_terminacion(self):  # Define el get del argumento fecha_terminacion
        return self.__fecha_terminacion


    def validar_nombre1(self): # Esta funcion sirve como ingreso de datos y validacion caracteres de ingreso 
        self.set_nombre_completo (input("Digite el nombre del aprendiz: ")) # Ingresa el nombre
        nombre_completo = self.get_nombre_completo()
        if not nombre_completo.isalpha(): # Valida que el ingreso solo sean caracteres alfabeticos
            print("La cadena debe contener solo letras digite nuevamente.")
            return self.validar_nombre1() # Si hay caracteres diferente envia mensaje y retorna al ingreso 


    def validar_documento1(self): # Esta funcion sirve como ingreso de datos y validacion caractres de ingreso 
        self.set_documento (input("Digite su numero de documento: ")) # Ingresa el documento
        nombre_completo = self.get_nombre_completo()
        dato_numerico = self.get_documento() # Valida que el ingreso solo sean caracteres numericos mayor a 1
        if not dato_numerico.isdigit() or len(dato_numerico) < 1:
            print("El dato debe ser un número entero positivo digite nuevamente.")
            return self.validar_documento1() # Si hay caracteres diferente envia mensaje y retorna al ingreso 


    def validar_ficha1(self): # Esta funcion sirve como ingreso de datos y validacion caractres de ingreso 
        self.set_ficha (input("Digite el numero de ficha al que pertenece: ")) # Ingresa la ficha 
        dato_numerico = self.get_ficha() # Valida que el ingreso solo sean caracteres numericos mayor a 1
        if not dato_numerico.isdigit() or len(dato_numerico) < 1:
            print("El dato debe ser un número entero positivo digite nuevamente.")
            return self.validar_ficha1() # Si hay caracteres diferente envia mensaje y retorna al ingreso 


    def validar_programa1(self): # Esta funcion sirve como ingreso de datos y validacion caractres de ingreso 
        self.set_programa (input("Digite el nombre del programa al que pertenece : "))  # Ingresa el programa
        programa = self.get_programa()
        if not programa.isalpha(): # Valida que el ingreso solo sean caracteres alfabeticos
            print("La cadena debe contener solo letras digite nuevamente.")
            return self.validar_programa1()   # Si hay caracteres diferente envia mensaje y retorna al ingreso 

    
    def validar_trimestre1(self): # Esta funcion sirve como ingreso de datos y validacion caractres de ingreso 
        self.set_numero_trimestre (input("Digite el numero de trimestre en que se encuentra: "))
        dato_numerico = self.get_numero_trimestre() # Ingresa el numero de trimestre en que se encuentra 
        if not dato_numerico.isdigit() or len(dato_numerico) < 1: # Valida que el ingreso solo sean caracteres numericos mayor a 1
            print("El dato debe ser un número entero positivo digite nuevamente.")
            return self.validar_trimestre1() # Si hay caracteres diferente envia mensaje y retorna al ingreso 


    def recibir_fecha_inicio1(self):  # Esta funcion sirve como ingreso de datos de la fecha 
        fecha_ingreso = input("Ingrese la fecha de ingreso a su etapa lectiva en formato dd-mm-yyyy: ") # Se ingresa fecha de acuerdo a formato
         
        try:        # Este arreglo sirve para recibir la fecha convertirla al formato datatime 
            fecha_ingreso = fecha_ingreso + ' 00:00:0'      
            fecha = datetime.strptime(fecha_ingreso, '%d-%m-%Y %H:%M:%S')
            return fecha_ingreso # Si la fecha no esta en el formato requerido hace un return 
        except ValueError: # Aqui se evalua el error 
            print("La fecha ingresada es inválida Por favor, inténtelo de nuevo.")
            return self.recibir_fecha_inicio1()# Se emite un mensaje de alerta y se retorna al ingreso para proceder nuevamente 


    def recibir_fecha_terminacion1(self): # Esta funcion sirve como ingreso de datos de la fecha 
        fecha_termino = input("Ingrese la fecha de termino de su etapa lectiva en formato dd-mm-yyyy: ") # Se ingresa fecha de acuerdo a formato
       
        try:  # Este arreglos sirve para recibir la fecha convertirla al formato datatime
            fecha_termino = fecha_termino + ' 00:00:0'
            fecha = datetime.strptime(fecha_termino, '%d-%m-%Y %H:%M:%S')
            return fecha_termino # Si la fecha no esta en el formato requerido hace un return 
        except ValueError: # Aqui se evalua el error 
            print("La fecha ingresada es inválida Por favor, inténtelo de nuevo.")
            return self.recibir_fecha_terminacion1() # Se emite un mensaje de alerta y se retorna al ingreso para proceder nuevamente 


    def leer_datos(self):
        # Esta funcion sirve para ingresar los datos por parte del usuario
        self.validar_nombre1() # Vincula el ingreso nombre
        self.validar_documento1()  # Vincula el ingreso documento
        self.validar_ficha1() # Vincula el ingreso ficha
        self.validar_programa1() # Vincula el ingreso programa
        self.validar_trimestre1() # Vincula el ingreso trimestre
        self.set_fecha_inicio(self.recibir_fecha_inicio1()) # Vincula el ingreso fecha inicio
        self.set_fecha_terminacion(self.recibir_fecha_terminacion1())  # Vincula el ingreso fecha termino
      

    def estado(self):
        estados = ["En induccion", "En formacion", "Aplazado", "Condicionado","Retirado"]
        emi= randint(0,len(estados) -1) # Esta funcion con un aleatorio de randint muestra el estado del aprendiz
        print("El estado del aprendiz es {0}".format(estados[emi]))


    def informacion_aprendiz(self):
        print("El nombre del aprendiz es:  {0} El numero de documento es :  {1} La ficha a la que pertenece es: {2} El programa donde esta matriculado es: {3}   El numero de trimestre es: {4}"
        "La fecha de inicio la etapa lectiva es:  {5} La fecha de terminacion de la etapa lectiva es:{6} " . format( self.get_nombre_completo(), self.get_documento(),
        self.get_ficha(), self.get_programa(), self.get_numero_trimestre(), self.get_fecha_inicio(), self.get_fecha_terminacion(),end =""))
    # Esta funcion imprime los datos ingresados por el usuario en leer datos 
      

    #----------------------ETAPA PRACTICA  -------------------------------------

class EtapaPractica (Aprendiz): # Definicion de la clase
 

    def __init__(self, documento = "", nombre_completo = "", ficha = 0, programa = "", modalidad = "", fecha_inicio = "", fecha_terminacion = "" ):
    #Creacion del constructor y sus argumentos  
       
        super ().__init__ (documento, nombre_completo,ficha, programa)
        # Definicion de los self de los argumentos que hereda de la subclase aprendiz

        self.__modalidad = modalidad
        self.__fecha_inicio = fecha_inicio  # Definicion self de los argumentos nuevos
        self.__fecha_terminacion = fecha_terminacion
   

    def set_modalidad(self, value): # Define el set del argumento modalidad
        self.__modalidad = value


    def get_modalidad(self):    # Define el get del argumento modalidad
        return self.__modalidad
    

    def set_fecha_inicio(self, value): # Define el set del argumento fecha_inicio
        self.__fecha_inicio = value


    def get_fecha_inicio(self):      # Define el get del argumento fecha_inicio     
        return self.__fecha_inicio


    def set_fecha_terminacion(self, value): # Define el set del argumento fecha_terminacion
        self.__fecha_terminacion = value


    def get_fecha_terminacion(self):  # Define el get del argumento fecha_terminacion 
        return self.__fecha_terminacion


    def validar_nombre(self): # Esta funcion sirve como ingreso de datos y validacion caracteres de ingreso 
        self.set_nombre_completo (input("Digite el nombre del aprendiz: ")) # Ingresa el nombre
        nombre_completo = self.get_nombre_completo()
        if not nombre_completo.isalpha(): # Valida que el ingreso solo sean caracteres alfabeticos
            print("La cadena debe contener solo letras digite nuevamente.") 
            return self.validar_nombre() # Si hay caracteres diferente envia mensaje y retorna al ingreso 


    def validar_numero(self): # Esta funcion sirve como ingreso de datos y validacion caracteres de ingreso 
        self.set_documento (input("Digite su numero de documento: ")) # Ingresa el documento
        dato_numerico = self.get_documento()
        if not dato_numerico.isdigit() or len(dato_numerico) < 1: # Valida que el ingreso solo sean caracteres numericos mayor a 1
            print("El dato debe ser un número entero positivo digite nuevamente.")
            return self.validar_numero()  # Si hay caracteres diferente envia mensaje y retorna al ingreso 


    def validar_ficha(self): # Esta funcion sirve como ingreso de datos y validacion caracteres de ingreso 
        self.set_ficha (input("Digite el numero de ficha al que pertenece: "))  # Ingresa la ficha
        dato_numerico = self.get_ficha() # Valida que el ingreso solo sean caracteres numericos mayor a 1
        if not dato_numerico.isdigit() or len(dato_numerico) < 1:
            print("El dato debe ser un número entero positivo digite nuevamente.")
            return self.validar_ficha() # Si hay caracteres diferente envia mensaje y retorna al ingreso 


    def validar_programa(self): # Esta funcion sirve como ingreso de datos y validacion caracteres de ingreso 
        self.set_programa (input("Digite el nombre del programa al que pertenece : "))   # Ingresa el programa 
        programa = self.get_programa()
        if not programa.isalpha(): # Valida que el ingreso solo sean caracteres alfabeticos
            print("La cadena debe contener solo letras digite nuevamente.")
            return self.validar_programa()  # Si hay caracteres diferente envia mensaje y retorna al ingreso 

    def validar_modalidad(self): # Esta funcion sirve como ingreso de datos y validacion caracteres de ingreso
        self.set_modalidad (input("En que modalidad se encuentra su etapa practica:  "))  # Ingresa la modalida
        modalidad = self.get_modalidad()
        if not modalidad.isalpha():# Valida que el ingreso solo sean caracteres alfabeticos
            print("La cadena debe contener solo letras digite nuevamente.")
            return self.validar_modalidad()  # Si hay caracteres diferente envia mensaje y retorna al ingreso 


    def recibir_fecha_inicio(self):   # Esta funcion sirve como ingreso de datos de la fecha 
        fecha_ingreso = input("Ingrese la fecha de ingreso a su etapa lectiva en formato dd-mm-yyyy: ") # Se ingresa fecha de acuerdo a formato
         
        try:  # Este arreglo sirve para recibir la fecha convertirla al formato datatime 
            fecha_ingreso = fecha_ingreso + ' 00:00:0'
            fecha = datetime.strptime(fecha_ingreso, '%d-%m-%Y %H:%M:%S')
            return fecha_ingreso # Si la fecha no esta en el formato requerido hace un return 
        except ValueError: # Aqui se evalua el error 
            print("La fecha ingresada es inválida Por favor, inténtelo de nuevo.")
            return self.recibir_fecha_inicio() # se emite un mensaje de alerta y se retorna al ingreso para proceder nueva mente 


    def recibir_fecha_terminacion(self):  # Esta funcion sirve como ingreso de datos de la fecha 
        fecha_termino = input("Ingrese la fecha de termino de su etapa lectiva en formato dd-mm-yyyy: ") # Se ingresa fecha de acuerdo a formato
       
        try: # Este arreglo sirve para recibir la fecha convertirla al formato datatime 
            fecha_termino = fecha_termino + ' 00:00:0'
            fecha = datetime.strptime(fecha_termino, '%d-%m-%Y %H:%M:%S')
            return fecha_termino # Si la fecha no esta en el formato requerido hace un return 
        except ValueError: # Aqui se evalua el error 
            print("La fecha ingresada es inválida Por favor, inténtelo de nuevo.")
            return self.recibir_fecha_terminacion() # Se emite un mensaje de alerta y se retorna al ingreso para proceder nuevamente 

    def leer_datos(self):
         # Esta funcion sirve para ingresar los datos por parte del usuario
        self.validar_nombre() # Vincula el ingreso nombre
        self.validar_numero() # Vincula el ingreso documento
        self.validar_ficha() # Vincula el ingreso ficha
        self.validar_programa() # Vincula el ingreso progrma
        self.validar_modalidad() # Vincula el ingreso modalidad 
        self.set_fecha_inicio(self.recibir_fecha_inicio()) # Vincula el ingreso fecha inicio 
        self.set_fecha_terminacion(self.recibir_fecha_terminacion()) # Vincula el ingreso fecha termino 

      
    def estado(self):
        estados = ["En induccion", "En formacion", "Aplazado", "Condicionado","Retirado"]
        emi= randint(0,len(estados)-1) # Esta funcion con un aleatorio de randint muestra el estado del aprendiz
        print("El estado del aprendiz es {0}".format(estados[emi]))


    def informacion_aprendiz(self):
        print("El nombre del aprendiz es:  {0} El numero de documento es :  {1} La ficha a la que pertenece es: {2} El programa donde esta matriculado es: {3}   La modalidad es : {4}"
        "La fecha de inicio la etapa lectiva es:  {5} La fecha de terminacion de la etapa lectiva es:{6} " . format( self.get_nombre_completo(), self.get_documento(),
        self.get_ficha(), self.get_programa(), self.get_modalidad(), self.get_fecha_inicio(), self.get_fecha_terminacion(),end =""))
    # Esta funcion imprime los datos ingresados por el usuario en leer datos 


     #----------------------INSTRUCTOR-------------------------------------

class Instructor (Persona): # Definicion de la subclase

    def __init__(self, documento, nombre_completo, profesion, salario_basico ): #Creacion del constructor y sus argumentos
        super ().__init__ (documento, nombre_completo)   # Definicion de los self de los argumentos que hereda de la superclase persona

        self.__profesion = profesion     # Definicion self de los argumentos nuevos
        self.__salario_basico = salario_basico
   
    def set_profesion(self, value): # Define el set del argumento profesion
        self.__profesion = value


    def get_profesion(self):       # Define el get del argumento profesion   
        return self.__profesion



    def set_salario_basico(self, value): # Define el set del argumento salario_basico
        self.__salario_basico = value


    def get_salario_basico(self):  # Define el get del argumento salario_basico
        return self.__salario_basico


#----------------------INSTRUCTOR PLANTA-------------------------------------

class InstructorPlanta (Instructor): # Definicion de la clase


    def __init__(self, documento = "", nombre_completo = "", profesion = "", salario_basico = 0, grado = 0, fecha_vinculacion = datetime):
     #Creacion del constructor y sus argumentos
        
        super ().__init__ (documento, nombre_completo, profesion, salario_basico)
        # Definicion de los self de los argumentos que hereda de la subclase instructor

        self.__grado = grado            # Definicion self de los argumentos nuevos
        self.__fecha_vinculacion = fecha_vinculacion
   
    def set_grado(self, value):    # Define el set del argumento grado
        self.__grado = value


    def get_grado(self):            # Define el get del argumento grado
        return self.__grado
        

    def set_fecha_vinculacion(self, value):  # Define el set del argumento fecha_vinculacion
        self.__fecha_vinculacion = value


    def get_fecha_vinculacion(self):    # Define el get del argumento fecha_vinculacion
        return self.__fecha_vinculacion


    def validar_nombre(self):  # Esta funcion sirve como ingreso de datos y validacion caracteres de ingreso 
        self.set_nombre_completo (input("Digite el nombre del instructor de planta: ")) # Ingresa el nombre
        nombre_completo = self.get_nombre_completo() 
        if not nombre_completo.isalpha():# Valida que el ingreso solo sean caracteres alfabeticos
            print("La cadena debe contener solo letras digite nuevamente.")
            return self.validar_nombre() # Si hay caracteres diferente envia mensaje y retorna al ingreso 

    
    def validar_documento(self): # Esta funcion sirve como ingreso de datos y validacion caracteres de ingreso 
        self.set_documento (input("Digite su numero de documento: ")) 
        dato_numerico = self.get_documento() # Ingresa el No de documento
        if not dato_numerico.isdigit() or len(dato_numerico) < 1: # Valida que el ingreso solo sean caracteres numericos 
            print("El dato debe ser un número entero positivo digite nuevamente.")
            return self.validar_documento() # Si hay caracteres diferente envia mensaje y retorna al ingreso

    
    def validar_profesion(self):# Esta funcion sirve como ingreso de datos y validacion caracteres de ingreso 
        self.set_profesion (input("Digite la profesion del instructor: "))
        profesion = self.get_profesion()  # Ingresa la profesion del instructor 
        if not profesion.isalpha(): # Valida que el ingreso solo sean caracteres alfabeticos
            print("La cadena debe contener solo letras digite nuevamente.")
            return self.validar_profesion() # Si hay caracteres diferente envia mensaje y retorna al ingreso

     
    def validar_grado(self): # Esta funcion sirve como ingreso de datos y validacion caracteres de ingreso
        self.set_grado (input("Escriba el grado del instructor : "))
        grade = self.get_grado() # Ingresa el grado del instructor
        if not grade.isdigit() or len(grade) > 1: # Valida que el ingreso solo sean caracteres numericos 
            print("El dato debe ser un número entero positivo digite nuevamente.")
            return self.validar_grado() # Si hay caracteres diferente envia mensaje y retorna al ingreso
             
      
    def recibir_fecha_vinculacion(self): # Esta funcion sirve como ingreso de datos de la fecha 
        fecha_vinculo = input("Digite la fecha de vinculacion del instructo en formato dd-mm-yyyy: ")
       
        try:
            fecha_vinculo = fecha_vinculo + ' 00:00:0'
            fecha = datetime.strptime(fecha_vinculo, '%d-%m-%Y %H:%M:%S')
            return fecha_vinculo # Si la fecha no esta en el formato requerido hace un return 
        except ValueError: # Aqui se evalua el error 
            print("La fecha ingresada es inválida Por favor, inténtelo de nuevo.")
            return self.recibir_fecha_vinculacion()  # Se emite un mensaje de alerta y se retorna al ingreso para proceder nuevamente


    def leer_datos(self):
       # Esta funcion sirve para ingresar los datos por parte del usuario
        self.validar_nombre() # Vincula el ingreso nombre
        self.validar_documento() # Vincula el ingreso del No de documento 
        self.validar_profesion() # Vincula el ingreso de la profesion 
        self.validar_grado() # Vincula el ingreso del gardo 
        self.set_fecha_vinculacion(self.recibir_fecha_vinculacion()) # Vincula el fecha de vinculacion 
    

    def informacion_instructor_planta(self):
        print("El nombre del instructor es:  {0} El numero de documento es :  {1} La profesion del instructor es es: {2} El grado del instructor es : {3}  La fecha de vincualcion del instructor es:{4} " . format( self.get_nombre_completo(), self.get_documento(), self.get_profesion(), self.get_grado(), self.get_fecha_vinculacion(), end =""))
    # Esta funcion imprime los datos ingresados por el usuario en leer datos 

    def estado(self):
        estados = ["En formacion", "En licencia", "En vacaciones", "prepensionado"]
        emi= randint(0,len(estados)-1)  # Esta funcion con un aleatorio de randint muestra el estado laboral del instructor
        print("El Instructor se encuentra en :  {0}".format(estados[emi]))

    def contrato(self):
        estados = ["Actvo", "Inactivo"]
        emi= randint(0,len(estados)-1) # Esta funcion con un aleatorio de randint muestra el estado del contrato del instructor 
        print("El contrato del instructor se encuentra :  {0}".format(estados[emi]))

    def sueldo (self):
        salario_basico = 1500000
        valor_grado = 100000 # Esta funcion calcula el suedo del instructor operando un salrio basico y el tiempo de antiguedad
        entrada_grado = int(self.__grado)
        print ( "El salario del instructor es ", salario_basico + (valor_grado * entrada_grado))
       

#----------------------INSTRUCTOR CONTRATO-------------------------------------


class InstructorContrato (Instructor): # Definicion de la clase


    def __init__(self, documento = 0, nombre_completo = "", profesion = "", salario_basico = 0, duracion_contrato = 0, fecha_vinculacion = datetime):
        #Creacion del constructor y sus argumentos

        super ().__init__ (documento, nombre_completo, profesion, salario_basico) 
        # Definicion de los self de los argumentos que hereda de la subclase instructor

        self.__duracion_contrato = duracion_contrato # Definicion self de los argumentos nuevos
        self.__fecha_vinculacion = fecha_vinculacion
   
    def set_duracion_contrato(self, value):  # Define el set del argumento contrato
        self.__duracion_contrato = value


    def get_duracion_contrato(self):    # Define el get del argumento contrato     
        return self.__duracion_contrato


    def set_fecha_vinculacion(self, value):  # Define el set del argumento fecha_vinculacion
        self.__fecha_vinculacion = value


    def get_fecha_vinculacion(self): # Define el get del argumento fecha_vinculacion
        return self.__fecha_vinculacion


    def validar_nombre(self):  # Esta funcion sirve como ingreso de datos y validacion caracteres de ingreso 
        self.set_nombre_completo (input("Digite el nombre del instructor de contrato: "))  # Ingresa el nombre
        nombre_completo = self.get_nombre_completo() 
        if not nombre_completo.isalpha(): # Valida que el ingreso solo sean caracteres alfabeticos
            print("La cadena debe contener solo letras digite nuevamente.")
            return self.validar_nombre()  # Si hay caracteres diferente envia mensaje y retorna al ingreso 

    
    def validar_documento(self): # Esta funcion sirve como ingreso de datos y validacion caracteres de ingreso 
        self.set_documento (input("Digite su numero de documento: ")) # Ingresa el No de documento 
        dato_numerico = self.get_documento()
        if not dato_numerico.isdigit() or len(dato_numerico) < 1: # Valida que el ingreso solo sean caracteres numericos 
            print("El dato debe ser un número entero positivo digite nuevamente.")
            return self.validar_documento()   # Si hay caracteres diferente envia mensaje y retorna al ingreso 

    
    def validar_profesion(self): # Esta funcion sirve como ingreso de datos y validacion caracteres de ingreso
        self.set_profesion (input("Digite la profesion del instructor de contrato: ")) 
        profesion = self.get_profesion() # Ingresa la profesion del instructor 
        if not profesion.isalpha(): # Valida que el ingreso solo sean caracteres alfabeticos 
            print("La cadena debe contener solo letras digite nuevamente.")
            return self.validar_profesion() # Si hay caracteres diferente envia mensaje y retorna al ingreso 


    def duracion_contrato(self): # Esta funcion sirve como ingreso de datos y validacion caracteres de ingreso
        self.set_duracion_contrato (input("Digite la cantidad de meses de duracion de su contrato: "))
        dato_numerico = self.get_duracion_contrato() # Ingresa la duracion del contrato 
        if not dato_numerico.isdigit() or len(dato_numerico) < 1: # Valida que el ingreso solo sean caracteres numericos 
            print("El dato debe ser un número entero positivo digite nuevamente.")
            return self.duracion_contrato() # Si hay caracteres diferente envia mensaje y retorna al ingreso

          
    def recibir_fecha_vinculacion(self): # Esta funcion sirve como ingreso de datos de la fecha
        fecha_vinculo = input("Digite la fecha de vinculacion del instructor en formato dd-mm-yyyy: ")
       
        try:
            fecha_vinculo = fecha_vinculo + ' 00:00:0'
            fecha = datetime.strptime(fecha_vinculo, '%d-%m-%Y %H:%M:%S')
            return fecha_vinculo # Si la fecha no esta en el formato requerido hace un return 
        except ValueError: # Aqui se evalua el error 
            print("La fecha ingresada es inválida Por favor, inténtelo de nuevo.")
            return self.recibir_fecha_vinculacion()   # Se emite un mensaje de alerta y se retorna al ingreso para proceder nuevamente


    def leer_datos(self):
         # Esta funcion sirve para ingresar los datos por parte del usuario

        self.validar_nombre()  # Vincula el ingreso nombre
        self.validar_documento() # Vincula el ingreso por No documento
        self.validar_profesion()  # Vincula el ingreso por profesion
        self.duracion_contrato()  # Vincula el ingreso por duracion de contrato
        self.set_fecha_vinculacion(self.recibir_fecha_vinculacion())  # Vincula el ingreso por fecha de vinculacion 
        

    def informacion_instructor_contrato(self):
        print("El nombre del instructor es:  {0}  */ El numero de documento es :  {1}  */ La profesion del instructor es es: {2}  */ La duracion del contrato es : {3}  */ La fecha de vincualcion del instructor es:{4} " . format( self.get_nombre_completo(), self.get_documento(), self.get_profesion(), self.get_duracion_contrato(), self.get_fecha_vinculacion(), end =""))
         # Esta funcion imprime los datos ingresados por el usuario en leer datos 
    

    # def contrato(self): # Esta funcion con un aleatorio de randint muestra el estado del contrato del instructor 
    #     estados = ["Actvo", "Inactivo"]
    #     emi= randint(0,len(estados)-1)
    #     print("El contrato del instructor se encuentra :  {0}".format(estados[emi]))


    def estado(self):
        estados = ["En formacion", "En licencia", "En vacaciones", "prepensionado"]
        emi= randint(0,len(estados)-1)
        print("El Instructor se encuentra en :  {0}".format(estados[emi]))

    def finalizacion_contrato(self):
        final = self.get_fecha_vinculacion() + timedelta(days=self.get_duracion_contrato()*30)
        print("La fecha de terminacion del contrato es {0}".format(final))


         # Esta funcion con un aleatorio de randint muestra el estado laboral del instructor

    # def sumar_meses (self,fecha, n_meses):
      
    #     fecha_objeto = datetime.strptime(fecha, "%d-%m-%Y")
    #     nueva_fecha = fecha_objeto + datetime.timedelta(days=30 * n_meses)
    #     nueva_fecha_str = nueva_fecha.strftime("%d-%m-%Y")


    #     fecha_ingresada = self.get_fecha_vinculacion()
    #     meses_a_sumar = self.get_duracion_contrato()

    #     resultado = sumar_meses(fecha_ingresada, meses_a_sumar)
    #     print(f"La nueva fecha después de sumar {meses_a_sumar} meses es: {resultado}")


    # def fecha_terminacion_contrato(self):
    #    fecha_inicial = self.get_fecha_vinculacion()
    # #    cantidad_contrato = self.__duracion_contrato
    #    fecha_terminacion = fecha_inicial + timedelta(days=5*30)
    #    print ("ESTA ES LA FECHA INICIAL", fecha_terminacion)
    # #    print("La fecha de terminación del contrato es: ", fecha_terminacion.strftime("%d/%m/%Y"))


    #    def sueldo (self):
    #     salario_basico = 1500000
    #     valor_grado = 100000
    #     entrada_grado = int(self.__grado)
    #     print ( "El salario del instructor es ", salario_basico + (valor_grado * entrada_grado))
       

   



    


