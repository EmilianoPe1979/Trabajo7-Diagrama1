from datetime import datetime, timedelta

# Fecha de inicialización
fecha_inicial = datetime(2024, 1, 1)

# Sumar 5 meses
fecha_terminacion = fecha_inicial + timedelta(days=5*30)

print("Fecha de terminación:", fecha_terminacion.strftime("%d/%m/%Y"))



def tiempo_contrato(self):
    try:
        fecha_vinculacion1 = self.__fecha_vinculacion
        fecha_vinculacion1 = datetime.strptime(fecha_vinculacion1, '%d-%m-%Y %H:%M:%S')
        hoy = datetime.now()
        if fecha_vinculacion1 < hoy:
            print("Su contrato ya ha terminado")
        else:
            tiempo_restante = fecha_vinculacion1 - hoy
            print(f"Tiempo restante del contrato: {tiempo_restante}")
    except ValueError as e:
        print('Error: La fecha debe estar en formato DD-MM-YYYY.')