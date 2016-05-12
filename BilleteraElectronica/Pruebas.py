'''
Created on May 12, 2016

Pruebas.py

Autores:
    Honorio Rodriguez 09-11023
    Carlos Gonzalez  10-10300
    
Descripcion:
    Casos de prueba para la realizacion de Billetera.py 

@author: carlos
'''

# Importamos lo que necesitamos
from Billetera import *
import unittest
import sys

# Creamos la clase para los casos de Prueba
class PruebasBilletera(unittest.TestCase):  
    '''  Caso Interior  '''
    def testClaseDueno(self):
        Angel = dueno('Angel', 'Martiñez Gonzalez', 21134902)
    
    '''  Caso Interior  '''
    def testClaseBilletera(self):
        Angel = dueno('Angel', 'Martiñez Gonzalez', 21134902)
        bill = BilleteraElectronica('255', Angel, 2201)
      
    '''  Caso Interior  '''  
    def testRecargar(self):
        Angel = dueno('Angel', 'Martiñez Gonzalez', 21134902)
        bill = BilleteraElectronica('255', Angel, 2201)
        bill.recargar(1500, '2201')
        self.assertEqual(1500, bill.saldo)
     
    '''  Caso Interior  '''   
    def testSaldo(self):
        Angel = dueno('Angel', 'Martiñez Gonzalez', 21134902)
        bill = BilleteraElectronica('255', Angel, 2201)
        self.assertEqual(0, bill.consultaSaldo())
        
    '''  Caso Interior  '''
    def testConsumir(self):
        Angel = dueno('Angel', 'Martiñez Gonzalez', 21134902)
        bill = BilleteraElectronica('255', Angel, 2201)
        bill.recargar(1500, '2201')
        bill.consumir(1000, '2201', 2201)
        self.assertEqual(500, bill.consultaSaldo())
        
    '''  Caso Interior  '''
    def testConsumirClave(self):
        Angel = dueno('Angel', 'Martiñez Gonzalez', 21134902)
        bill = BilleteraElectronica('255', Angel, 2201)
        bill.recargar(1500, '2201')
        bill.consumir(1000, '2201', 2541)
        self.assertEqual(1500, bill.consultaSaldo())
        
    '''  Caso Interior  '''
    def testSaldoSuficiente(self):
        Angel = dueno('Angel', 'Martiñez Gonzalez', 21134902)
        bill = BilleteraElectronica('255', Angel, 2201)
        bill.recargar(1500, '2201')
        bill.consumir(2000, '2201', 2541)
        self.assertEqual(1500, bill.consultaSaldo())
        
    '''  Caso Malicioso  '''
    def testSaldoNegativo(self):
        Angel = dueno('Angel', 'Martiñez Gonzalez', 21134902)
        bill = BilleteraElectronica('255', Angel, 2201)
        bill.recargar(-1500, '2201')
        self.assertEqual(0, bill.consultaSaldo())
        
    '''  Caso Malicioso  '''
    def testMontoNegativo(self):
        Angel = dueno('Angel', 'Martiñez Gonzalez', 21134902)
        bill = BilleteraElectronica('255', Angel, 2201)
        bill.consumir(-2000, '2201', 2541)
        self.assertEqual(0, bill.consultaSaldo())
        
    '''  Caso Interior  '''
    def testTransaccionesRecar(self):
        Angel = dueno('Angel', 'Martiñez Gonzalez', 21134902)
        bill = BilleteraElectronica('255', Angel, 2201)
        bill.recargar(4000, '2201')
        bill.recargar(20, '2201')
        bill.recargar(50, '2201')
        bill.recargar(30, '2201')
        bill.recargar(700, '2201')
        self.assertEqual(5, len(bill.credito.creditos))
      
    '''  Caso Malicioso  '''
    def testCedulaNegativa(self):
        Angel = dueno('Angel', 'Martiñez Gonzalez', -21134902)
        self.assertEqual(None, Angel.ci)
        
    '''  Caso Malicioso  '''
    def testCedulaInvalida(self):
        Angel = dueno('Angel', 'Martiñez Gonzalez', 'hg4')
        self.assertEqual(None, Angel.ci)
        
    '''  Caso Frontera  '''  
    def testCedula1Digito(self):
        Angel = dueno('Angel', 'Martiñez Gonzalez', 2)
        self.assertEqual(1, len(str(Angel.ci)))
        
    '''  Caso Frontera  '''
    def testCedula10Digitos(self):
        Angel = dueno('Angel', 'Martiñez Gonzalez', 2254863254)
        self.assertEqual(10, len(str(Angel.ci)))
       
    '''  Caso Esquina  ''' 
    def testCedulaCero(self):
        Angel = dueno('Angel', 'Martiñez Gonzalez', 0)
        self.assertEqual(None, Angel.ci)
     
    '''  Caso Esquina  '''    
    def testCedula11Digitos(self):
        Angel = dueno('Angel', 'Martiñez Gonzalez', 22222222222)
        self.assertEqual(None, Angel.ci)
    
    '''  Caso Interior  '''      
    def testTransaccionesConsu(self):
        Angel = dueno('Angel', 'Martiñez Gonzalez', 21134902)
        bill = BilleteraElectronica('255', Angel, 2201)
        bill.recargar(10000, '2201')
        bill.consumir(2000, '2201', 2201)
        bill.consumir(100, '2201', 2201)
        bill.consumir(4000, '2201', 2201)
        bill.consumir(30, '2201', 2201)
        bill.consumir(200, '2201', 2201)
        bill.consumir(100, '2201', 2201)
        self.assertEqual(6, len(bill.debito.debitos))
        
    '''  Caso Esquina  ''' 
    def testMontoMaximo(self):
        Angel = dueno('Angel', 'Martiñez Gonzalez', 21134902)
        bill = BilleteraElectronica('255', Angel, 2201)
        bill.recargar(sys.maxsize, '2201')
        self.assertEqual(sys.maxsize, bill.consultaSaldo())
        
    '''  Caso Frontera  ''' 
    def testMontoMinimo(self):
        Angel = dueno('Angel', 'Martiñez Gonzalez', 21134902)
        bill = BilleteraElectronica('255', Angel, 2201)
        bill.recargar(1, '2201')
        self.assertEqual(1, bill.consultaSaldo())
        
    '''  Caso Malicioso  '''            
    def testPinNoNumerico(self):
        Angel = dueno('Angel', 'Martiñez Gonzalez', 21134902)
        bill = BilleteraElectronica('255', Angel, 'hgf')
        self.assertEqual(None, bill.pin)
        
    '''  Caso Malicioso  ''' 
    def testNombresCarEspeciales(self):
        Angel = dueno('Ángel_ñ', 'Martiñez-Gonzalez', 21134902)
        self.assertEqual(True, isinstance(Angel.nombres,str))
       
    '''  Caso Frontera  '''  
    def testConsumoMaximo(self):
        Angel = dueno('Angel', 'Martiñez Gonzalez', 21134902)
        bill = BilleteraElectronica('255', Angel, 2201)
        bill.recargar(50000, '2201')
        bill.consumir(bill.consultaSaldo(), '2201', 2201)
        self.assertEqual(0, bill.saldo)
        
    
 
        