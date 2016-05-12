'''
Created on May 12, 2016

@author: carlos
'''
from Billetera import *
import unittest
import sys

class PruebasBilletera(unittest.TestCase):  
    def testClaseDueno(self):
        Angel = dueno('Angel', 'Martiñez Gonzalez', 21134902)
    
    def testClaseBilletera(self):
        Angel = dueno('Angel', 'Martiñez Gonzalez', 21134902)
        bill = BilleteraElectronica('255', Angel, 2201)
        
    def testRecargar(self):
        Angel = dueno('Angel', 'Martiñez Gonzalez', 21134902)
        bill = BilleteraElectronica('255', Angel, 2201)
        bill.recargar(1500, '2201')
        self.assertEqual(1500, bill.saldo)
        
    def testSaldo(self):
        Angel = dueno('Angel', 'Martiñez Gonzalez', 21134902)
        bill = BilleteraElectronica('255', Angel, 2201)
        self.assertEqual(0, bill.consultaSaldo())
        
    def testConsumir(self):
        Angel = dueno('Angel', 'Martiñez Gonzalez', 21134902)
        bill = BilleteraElectronica('255', Angel, 2201)
        bill.recargar(1500, '2201')
        bill.consumir(1000, '2201', 2201)
        self.assertEqual(500, bill.consultaSaldo())
        
    def testConsumirClave(self):
        Angel = dueno('Angel', 'Martiñez Gonzalez', 21134902)
        bill = BilleteraElectronica('255', Angel, 2201)
        bill.recargar(1500, '2201')
        bill.consumir(1000, '2201', 2541)
        self.assertEqual(1500, bill.consultaSaldo())
        
    def testSaldoSuficiente(self):
        Angel = dueno('Angel', 'Martiñez Gonzalez', 21134902)
        bill = BilleteraElectronica('255', Angel, 2201)
        bill.recargar(1500, '2201')
        bill.consumir(2000, '2201', 2541)
        self.assertEqual(1500, bill.consultaSaldo())
        
    
    def testSaldoNegativo(self):
        Angel = dueno('Angel', 'Martiñez Gonzalez', 21134902)
        bill = BilleteraElectronica('255', Angel, 2201)
        bill.recargar(-1500, '2201')
        self.assertEqual(0, bill.consultaSaldo())
        
        
    def testMontoNegativo(self):
        Angel = dueno('Angel', 'Martiñez Gonzalez', 21134902)
        bill = BilleteraElectronica('255', Angel, 2201)
        bill.consumir(-2000, '2201', 2541)
        self.assertEqual(0, bill.consultaSaldo())
        
    def testTransaccionesRecar(self):
        Angel = dueno('Angel', 'Martiñez Gonzalez', 21134902)
        bill = BilleteraElectronica('255', Angel, 2201)
        bill.recargar(4000, '2201')
        bill.recargar(20, '2201')
        bill.recargar(50, '2201')
        bill.recargar(30, '2201')
        bill.recargar(700, '2201')
        self.assertEqual(5, len(bill.credito.creditos))
      
    
    def testCedulaNegativa(self):
        Angel = dueno('Angel', 'Martiñez Gonzalez', -21134902)
        self.assertEqual(None, Angel.ci)
        
    def testCedulaInvalida(self):
        Angel = dueno('Angel', 'Martiñez Gonzalez', 'hg4')
        self.assertEqual(None, Angel.ci)
        
        
    def testCedula1Digito(self):
        Angel = dueno('Angel', 'Martiñez Gonzalez', 2)
        self.assertEqual(1, len(str(Angel.ci)))
        
    def testCedula10Digitos(self):
        Angel = dueno('Angel', 'Martiñez Gonzalez', 2254863254)
        self.assertEqual(10, len(str(Angel.ci)))
        
    def testCedulaCero(self):
        Angel = dueno('Angel', 'Martiñez Gonzalez', 0)
        self.assertEqual(None, Angel.ci)
        
    def testCedula11Digitos(self):
        Angel = dueno('Angel', 'Martiñez Gonzalez', 22222222222)
        self.assertEqual(None, Angel.ci)
    
    '''      
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
        
    def testMontoMaximo(self):
        Angel = dueno('Angel', 'Martiñez Gonzalez', 21134902)
        bill = BilleteraElectronica('255', Angel, 2201)
        bill.recargar(sys.maxsize, '2201')
        self.assertEqual(sys.maxsize, bill.consultaSaldo())
        
    def testMontoMinimo(self):
        Angel = dueno('Angel', 'Martiñez Gonzalez', 21134902)
        bill = BilleteraElectronica('255', Angel, 2201)
        bill.recargar(1, '2201')
        self.assertEqual(1, bill.consultaSaldo())
        
     Casos Maliciosos
            
    def testPinNoNumerico(self):
        Angel = dueno('Angel', 'Martiñez Gonzalez', 21134902)
        bill = BilleteraElectronica('255', Angel, 'hgf')
        self.assertEqual(None, bill.pin)
        
    def testNombresCarEspeciales(self):
        Angel = dueno('Ángel_ñ', 'Martiñez-Gonzalez', 21134902)
        self.assertEqual(True, isinstance(Angel.nombres,str))
        
    def testConsumoMaximo(self):
        Angel = dueno('Angel', 'Martiñez Gonzalez', 21134902)
        bill = BilleteraElectronica('255', Angel, 2201)
        bill.recargar(50000, '2201')
        bill.consumir(bill.consultaSaldo(), '2201', 2201)
        self.assertEqual(0, bill.saldo)
        
    
 ''' 
        