'''
Created on May 12, 2016

@author: carlos
'''
from Billetera import *
import unittest

class PruebasBilletera(unittest.TestCase):
    def testClaseVacia(self):
        bill = billeteraElectronica('255')
        
        