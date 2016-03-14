from unittest import TestCase
from Procesador import *

class TestProcesador(TestCase):

    def test_contador(self):
        lista = Procesador().contador("")
        self.assertEquals(Procesador().contador(""),[0,0,0],"Lista Vacia")

    def test_contar_1 (self):
        lista = Procesador().contador("")
        self.assertEquals(Procesador().contador("4"),[1,4,4],"Lista con un elemento")

    def test_contar_2 (self):
        self.assertEquals(Procesador().contador("3,2"),[2,2,3],"Lista con dos elementos")

    def test_contar_n (self):
        self.assertEquals(Procesador().contador("2,3,4,1"),[4,1],"Lista con cuatro elementos")



