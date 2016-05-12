'''
Created on May 12, 2016

Billetera.py

Autores:
    Honorio Rodriguez 09-11023
    Carlos Gonzalez  10-10300
    
Descripcion:
    Billetera Virtual para la realizacion de transacciones y consumos

@author: carlos
'''

# Importamos lo necesario para la ejecucion del programa
from datetime import *
import calendar
import sys
import time

# Creamos la clase dueno que aceptara nombres, apellidos, y un numero de cedula
class dueno:
    # Iniciamos la clase
    def __init__(self, nombres, apellidos, ci):
        if isinstance(ci,int) and ci>0 and 1<=len(str(ci))<=10:
            self.nombres = nombres
            self.apellidos = apellidos
            self.ci = ci
        # De no cumplir la restricciones de la cedula sera un dueno nulo
        else:
            self.nombres = None
            self.apellidos = None
            self.ci = None

# Una clase transaccion para definir las recargas y consumos dentro de la billetera
class transaccion:
    # Se inicia con un monto una fecha y un id del establecimiento
    def __init__(self, monto, fecha, idEst):
        self.monto = monto
        self.fecha = fecha
        self.id = idEst 
    
# Creamos la clase credito para guardar todas las transacciones de recargas realizadas    
class Creditos:
    # Iniciamos la clase
    def __init__(self):
        self.creditos = []
     
    # Creamos funcion para agregar transaccion   
    def nuevaRecarga(self, transaccion):
        self.creditos.append(transaccion)
                
# Creamos la clase debitos para guardar todas las transacciones de recargas realizadas                 
class Debitos:
    # Iniciamos la clase
    def __init__(self):
        self.debitos = []
    # Definimos funcion para agragar nuevo consumo a la lista  
    def nuevoConsumo(self, transaccion):
        self.debitos.append(transaccion)
        
# Definimos la clase BilleteraElectronica
class BilleteraElectronica:
    # Iniciamos la clase
    def __init__(self, identificador, dueno, pin):
        # Verificamos que el pin introducido sea numerico
        if isinstance(pin,int):
            self.identificador = identificador
            self.dueno = dueno
            self.pin = pin
            self.saldo = 0
            self.credito = Creditos()
            self.debito = Debitos()
            
        # De no ser numerico La Billetera sera nula   
        else:
            self.identificador = None
            self.dueno = None
            self.pin = None
            self.saldo = None
            self.credito = None
            self.debito = None 
             
    # Definimos funcion consultar saldo para saber el saldo de la billetera            
    def consultaSaldo(self):
        return self.saldo
     
    # Definimos la funcion recarga para realizar una recarga a la cuenta  
    def recargar(self, monto, idEst):
        # Verificamos que el monto no sea negativo
        if monto > 0:
            fecha = time.strftime("%d/%m/%y")
            cre = transaccion(monto, fecha, idEst)
            self.credito.nuevaRecarga(cre)
            self.saldo = self.saldo + monto
            
    # Definimos la funcion consumir para realiar un nuevo consumo   
    def consumir(self, monto, idEst, pin):
        # Verificamos que el monto no sea negativo, el pin el correcto y
        # el monto mayor a cero
        if (self.saldo >= monto  and self.pin == pin and monto > 0):
            fecha = time.strftime("%d/%m/%y")
            deb = transaccion(monto, fecha, idEst)
            self.debito.nuevoConsumo(deb)
            self.saldo = self.saldo - monto
            

            
        
    
