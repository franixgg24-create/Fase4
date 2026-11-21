
import re

from entidades import Entidad
from excepciones import DatosInvalidosError


class Cliente(Entidad):

    def __init__(self, identificador, nombre, documento, correo, telefono):
        super().__init__(identificador)

        if not isinstance(nombre, str) or not nombre.strip():
            raise DatosInvalidosError(
                "El nombre del cliente no puede estar vacio."
            )

        if not isinstance(documento, str) or not documento.isdigit():
            raise DatosInvalidosError(
                "El documento debe contener solo numeros."
            )

        if not isinstance(telefono, str) or not telefono.isdigit():
            raise DatosInvalidosError(
                "El telefono debe contener solo numeros."
            )

        if not isinstance(correo, str) or not re.fullmatch(
            r"[\w.-]+@[\w.-]+\.[a-zA-Z]{2,}",
            correo
        ):
            raise DatosInvalidosError(
                "El correo electronico no es valido."
            )

        self.__nombre = nombre.strip()
        self.__documento = documento
        self.__correo = correo
        self.__telefono = telefono

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
