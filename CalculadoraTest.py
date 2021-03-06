from unittest import TestCase

__author__ = 'nazly'

from Calculadora import Calculadora

class CalculadoraTest(TestCase):
    def test_sumar(self):
        self.assertEqual(Calculadora().sumar(""),0,"Cadena vacia")

    def test_sumar_unacadena(self):
        self.assertEqual(Calculadora().sumar("1"),1,"Un numero")

    def test_sumar_cadenaConUnNumero(self):
        self.assertEqual(Calculadora().sumar("1"),1,"Un numero")
        self.assertEqual(Calculadora().sumar("2"),2,"Un numero")

    def test_sumar_cadenaConUnNumero(self):
        self.assertEqual(Calculadora().sumar("1,3"), 4, "Dos numeros")