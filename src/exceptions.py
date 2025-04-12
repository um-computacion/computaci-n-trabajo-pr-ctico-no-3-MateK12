class NumeroDebeSerPositivo(Exception):
    def __init__(self):
        super().__init__('Ingrese un numero positivo')
    pass
