'''
Created on May 12, 2016

@author: carlos
'''
class dueno:
    def __init__(self, nombres, apellidos, ci):
        self.nombres = nombres
        self.apellidos = apellidos
        self.ci = ci

class billeteraElectronica:
    def __init__(self, identificador, dueno, pin):
        self.identificador = identificador
        self.dueno = dueno
        self.pin = pin
    