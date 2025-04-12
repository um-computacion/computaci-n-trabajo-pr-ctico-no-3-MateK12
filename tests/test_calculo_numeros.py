import unittest
from src.exceptions import (
    ingrese_numero,
    NumeroDebeSerPositivo,
)
from unittest.mock import patch

class TestCalculoNumeros(unittest.TestCase):


    @patch('builtins.input',return_value='AAA')
    def test_ingreso_letras(self, patch_input):
        with self.assertRaises(ValueError):
            ingrese_numero()

    @patch('builtins.input',return_value='-100')
    def test_ingreso_negativo(self, patch_input):
        with self.assertRaises(NumeroDebeSerPositivo):
            ingrese_numero()

    @patch('builtins.input',return_value='-10')
    def test_ingreso_negativo_1(self,mock_input):
        with self.assertRaises(NumeroDebeSerPositivo):
            ingrese_numero()
if __name__ == '__main__':
    unittest.main() 