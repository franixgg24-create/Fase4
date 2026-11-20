from abc import ABC, abstractmethod


class Entidad(ABC):

    def __init__(self, identificador):

        if not isinstance(identificador, str) or not identificador.strip():
            raise ValueError("El identificador es obligatorio.")

        self.__identificador = identificador.strip()

    @property
    def identificador(self):
        return self.__identificador

    @abstractmethod
    def mostrar_informacion(self):
        pass