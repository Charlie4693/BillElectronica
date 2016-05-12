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
        
        
class Creditos:
    def __init__(self):
        self.creditos = []
        
    def nuevaRecarga(self, transaccion):
        self.creditos.append(transaccion)
                
               
class Debitos:
    def __init__(self):
        self.debitos = []
        
    def nuevoConsumo(self, transaccion):
        self.debitos.append(transaccion)
        

class BilleteraElectronica:
    def __init__(self, identificador, dueno, pin):
        if isinstance(pin,int):
            self.identificador = identificador
            self.dueno = dueno
            self.pin = pin
            self.saldo = 0
            self.credito = Creditos()
            self.debito = Debitos()
            
        else:
            self.identificador = None
            self.dueno = None
            self.pin = None
            self.saldo = None
            self.credito = None
            self.debito = None  
                
    def consultaSaldo(self):
        return self.saldo
       
    def recargar(self, monto, idEst):
        if monto > 0:
            fecha = time.strftime("%d/%m/%y")
            cre = transaccion(monto, fecha, idEst)
            self.credito.nuevaRecarga(cre)
            self.saldo = self.saldo + monto
        
    def consumir(self, monto, idEst, pin):
        if (self.saldo >= monto  and self.pin == pin and monto > 0):
            fecha = time.strftime("%d/%m/%y")
            deb = transaccion(monto, fecha, idEst)
            self.debito.nuevoConsumo(deb)
            self.saldo = self.saldo - monto
            

            
        
    
