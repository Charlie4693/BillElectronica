'''
Created on May 12, 2016

@author: carlos
'''
from Billetera import *
import unittest

class PruebasBilletera(unittest.TestCase):  
    def testClaseBilletera(self):
        Angel = dueno('Angel', 'Martiñez Gonzalez', 21134902)
        bill = BilleteraElectronica('255', Angel, 2201)
        