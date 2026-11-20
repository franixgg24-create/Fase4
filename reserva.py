
from excepciones import DatosInvalidosError


class Reserva:

    def __init__(self, identificador, cliente, servicio, cantidad):
        if not identificador:
            raise DatosInvalidosError("El identificador de la reserva es obligatorio.")

        if cantidad <= 0:
            raise DatosInvalidosError("La cantidad debe ser mayor que cero.")

        self.__identificador = identificador
        self.__cliente = cliente
        self.__servicio = servicio
        self.__cantidad = cantidad
        self.__costo_total = servicio.calcular_costo(cantidad)

    @property
    def identificador(self):
        return self.__identificador

    @property
    def cliente(self):
        return self.__cliente

    @property
    def servicio(self):
        return self.__servicio

    @property
    def cantidad(self):
        return self.__cantidad

    @property
    def costo_total(self):
        return self.__costo_total

    def mostrar_reserva(self):
        return (
            f"Reserva: {self.__identificador}\n"
            f"Cliente: {self.cliente.nombre}\n"
            f"{self.servicio.mostrar_informacion()}\n"
            f"Cantidad: {self.__cantidad}\n"
            f"Costo total: ${self.__costo_total:,.2f}"
        )
