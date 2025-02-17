# Definir una clase de excepción personalizada para manejar el caso cuando no se encuentran productos
# La clase hereda de la excepción base 'Exception'
class ProductNotFoundException(Exception):
    
    # El constructor de la clase acepta un mensaje de error personalizado. Si no se proporciona, usa el mensaje por defecto
    def __init__(self, message="Products not found"):
        self.message = message  # Asigna el mensaje de error a un atributo de la instancia
        super().__init__(self.message)  # Llama al constructor de la clase base 'Exception' con el mensaje