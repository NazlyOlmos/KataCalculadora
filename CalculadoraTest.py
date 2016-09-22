from unittest import TestCase

__author__ = 'nazly'

import Calculadora

class CalculadoraTest(TestCase):
    def test_sumar(self):
        self.assertEqual(Calculadora().sumar(""),0,"Cadena vacia")
