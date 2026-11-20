
import re

from entidades import Entidad
from excepciones import DatosInvalidosError


class Cliente(Entidad):

    def __init__(self, identificador, nombre, documento, correo, telefono):
        super().__init__(identificador)

        self.__nombre = nombre
        self.__documento = documento
        self.__correo = correo
        self.__telefono = telefono

        self.validar_datos()

    def validar_datos(self):
        if not self.__nombre or not self.__nombre.strip():
            raise DatosInvalidosError("El nombre del cliente no puede estar vacio.")

        if not self.__documento.isdigit():
            raise DatosInvalidosError("El documento debe contener solo numeros.")

        if not re.match(r"^[\w.-]+@[\w.-]+\.[a-zA-Z]{2,}$", self.__correo):
            raise DatosInvalidosError("El correo electronico no es valido.")

        if not self.__telefono.isdigit():
            raise DatosInvalidosError("El telefono debe contener solo numeros.")

    @property
    def nombre(self):
        return self.__nombre

    @property
    def documento(self):
        return self.__documento

    @property
    def correo(self):
        return self.__correo

    @property
    def telefono(self):
        return self.__telefono

    def mostrar_informacion(self):
        return (
            f"Identificador: {self.identificador}\n"
            f"Nombre: {self.__nombre}\n"
            f"Documento: {self.__documento}\n"
            f"Correo: {self.__correo}\n"
            f"Telefono: {self.__telefono}"
        )
