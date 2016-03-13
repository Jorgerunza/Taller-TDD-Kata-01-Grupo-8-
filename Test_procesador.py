from unittest import TestCase
from Procesador import *

class TestProcesador(TestCase):

    def test_contador(self):
        self.assertEquals(Procesador().contador(""),0,"Lista Vacia")

    def test_contar_1 (self):
        self.assertEquals(Procesador().contador("1"),1,"Lista con un elemento")

