from unittest import TestCase
from Procesador import *

class TestProcesador(TestCase):
    def test_contador(self):
        self.assertEquals(Procesador().contador(""),0,"Lista Vacia")
