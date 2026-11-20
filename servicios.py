
from abc import ABC, abstractmethod

from entidades import Entidad
from excepciones import DatosInvalidosError


class Servicio(Entidad, ABC):

    def __init__(self, identificador, nombre, tarifa):
        super().__init__(identificador)

        if not nombre or not nombre.strip():
            raise DatosInvalidosError("El nombre del servicio es obligatorio.")

        if tarifa <= 0:
            raise DatosInvalidosError("La tarifa debe ser mayor que cero.")

        self.__nombre = nombre
        self.__tarifa = tarifa

    @property
    def nombre(self):
        return self.__nombre

    @property
    def tarifa(self):
        return self.__tarifa

    @abstractmethod
    def calcular_costo(self, cantidad):
        pass

    @abstractmethod
    def mostrar_informacion(self):
        pass


class ReservaSalas(Servicio):

    def calcular_costo(self, cantidad):
        return self.tarifa * cantidad

    def mostrar_informacion(self):
        return f"Servicio: {self.nombre} - Reserva de salas"


class AlquilerEquipos(Servicio):

    def calcular_costo(self, cantidad):
        return self.tarifa * cantidad

    def mostrar_informacion(self):
        return f"Servicio: {self.nombre} - Alquiler de equipos"


class AsesoriaEspecializada(Servicio):

    def calcular_costo(self, cantidad):
        return self.tarifa * cantidad

    def mostrar_informacion(self):
        return f"Servicio: {self.nombre} - Asesoria especializada"
