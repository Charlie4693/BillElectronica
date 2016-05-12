'''
Created on May 12, 2016

@author: carlos
'''
from Billetera import *
import unittest

class PruebasBilletera(unittest.TestCase):
    '''
    def testClaseVacia(self):
        bill = billeteraElectronica('255')
    '''   
    ''' 
    def testClaseDueno(self):
        Angel = dueno('Angel', 'Martinez Gonzalez', 21134902)
        bill = billeteraElectronica('255', Angel)
    '''    
    def testPin(self):
        Angel = dueno('Angel', 'Martinez Gonzalez', 21134902)
        bill = billeteraElectronica('255', Angel, 2201)
        