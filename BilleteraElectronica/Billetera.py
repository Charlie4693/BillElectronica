'''
Created on May 12, 2016

@author: carlos
'''

from datetime import *
import calendar
import sys
import time

class dueno:
    def __init__(self, nombres, apellidos, ci):
        self.nombres = nombres
        self.apellidos = apellidos
        self.ci = ci
        
class transaccion:
    def __init__(self, monto, fecha, idEst):
        self.monto = monto
        self.fecha = fecha
        self.id = idEst 
        
    def __str__(self):
        cadena= 'Monto: '+self.monto+', fecha: '+self.fecha +', Id Establecimiento: ' +self.idEst 
        return cadena
        
        
class creditos:
    def __init__(self):
        self.creditos = []
        
    def nuevaRecarga(self, transaccion):
        self.creditos.append(transaccion)
                
               
class debitos:
    def __init__(self):
        self.debitos = []
        
    def nuevoConsumo(self, transaccion):
        self.debitos.append(transaccion)

class BilleteraElectronica:
    def __init__(self, identificador, dueno, pin):
        self.identificardor = identificador
        self.dueno = dueno
        self.pin = pin
        self.saldo = 0
        self.creditos = creditos()
        self.debitos = debitos()
                
    def saldo(self):
        pass
       
    def recargar(self, monto, idEst):
        pass
        
    def consumir(self, monto, idEst, pin):
        pass