class NumeroDebeSerPositivo(Exception):
    def __init__(self):
        super().__init__("El número debe ser positivo")
    pass


def ingrese_numero():
    
    entrada = input("Ingrese un número: ")
    try:
        numero = int(entrada)
        if numero < 0:
            raise NumeroDebeSerPositivo()
        return numero
    except ValueError:
        raise ValueError("La entrada debe ser un número válido")
    
# ingrese_numero()