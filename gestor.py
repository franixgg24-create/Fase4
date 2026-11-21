
import json
from pathlib import Path

from cliente import Cliente
from servicios import (
    Servicio,
    ReservaSalas,
    AlquilerEquipos,
    AsesoriaEspecializada
)
from reserva import Reserva
from excepciones import (
    DatosInvalidosError,
    ClienteNoEncontradoError,
    ServicioNoDisponibleError
)
from logs import obtener_logger


class Gestor:

    def __init__(self):
        self.__clientes = []
        self.__servicios = []
        self.__reservas = []
        self.__logger = obtener_logger()

        self.__ruta_datos = Path(__file__).parent / "datos"
        self.__ruta_datos.mkdir(exist_ok=True)

        self.__archivo_clientes = self.__ruta_datos / "clientes.json"
        self.__archivo_servicios = self.__ruta_datos / "servicios.json"
        self.__archivo_reservas = self.__ruta_datos / "reservas.json"

        self.__cargar_datos()

        self.__logger.info("Sistema iniciado correctamente.")

    def registrar_cliente(self, cliente):

        if not isinstance(cliente, Cliente):
            raise DatosInvalidosError(
                "El objeto no es un cliente valido."
            )

        if self.buscar_cliente(cliente.documento):
            raise DatosInvalidosError(
                "El documento del cliente ya existe."
            )

        for c in self.__clientes:
            if c.identificador == cliente.identificador:
                raise DatosInvalidosError(
                    "El identificador del cliente ya existe."
                )

        self.__clientes.append(cliente)
        self.__guardar_datos()

        self.__logger.info(
            f"Cliente registrado: {cliente.nombre}"
        )

    def registrar_servicio(self, servicio):

        if not isinstance(servicio, Servicio):
            raise DatosInvalidosError(
                "El objeto no es un servicio valido."
            )

        if self.buscar_servicio(servicio.identificador):
            raise DatosInvalidosError(
                "El servicio ya existe."
            )

        self.__servicios.append(servicio)
        self.__guardar_datos()

        self.__logger.info(
            f"Servicio registrado: {servicio.nombre}"
        )

    def buscar_cliente(self, documento):

        for cliente in self.__clientes:
            if cliente.documento == documento:
                return cliente

        return None

    def buscar_servicio(self, identificador):

        for servicio in self.__servicios:
            if servicio.identificador == identificador:
                return servicio

        return None

    def crear_reserva(
        self, identificador, documento, id_servicio, cantidad
    ):

        cliente = self.buscar_cliente(documento)

        if cliente is None:
            raise ClienteNoEncontradoError(
                "El cliente no existe."
            )

        servicio = self.buscar_servicio(id_servicio)

        if servicio is None:
            raise ServicioNoDisponibleError(
                "El servicio no existe."
            )

        reserva = Reserva(
            identificador, cliente, servicio, cantidad
        )

        self.__reservas.append(reserva)
        self.__guardar_datos()

        self.__logger.info(
            f"Reserva creada: {identificador}"
        )

        return reserva

    def listar_clientes(self):
        return self.__clientes.copy()

    def listar_servicios(self):
        return self.__servicios.copy()

    def listar_reservas(self):
        return self.__reservas.copy()

    def __guardar_datos(self):

        clientes = [
            {
                "identificador": c.identificador,
                "nombre": c.nombre,
                "documento": c.documento,
                "correo": c.correo,
                "telefono": c.telefono
            }
            for c in self.__clientes
        ]

        servicios = [
            {
                "identificador": s.identificador,
                "nombre": s.nombre,
                "tarifa": s.tarifa,
                "tipo": type(s).__name__
            }
            for s in self.__servicios
        ]

        reservas = [
            {
                "identificador": r.identificador,
                "documento_cliente": r.cliente.documento,
                "id_servicio": r.servicio.identificador,
                "cantidad": r.cantidad
            }
            for r in self.__reservas
        ]

        archivos = [
            (self.__archivo_clientes, clientes),
            (self.__archivo_servicios, servicios),
            (self.__archivo_reservas, reservas)
        ]

        for ruta, datos in archivos:
            with open(ruta, "w", encoding="utf-8") as archivo:
                json.dump(
                    datos,
                    archivo,
                    indent=4,
                    ensure_ascii=False
                )

        self.__logger.info(
            "Datos guardados correctamente."
        )

    def __cargar_datos(self):

        try:
            for ruta in (
                self.__archivo_clientes,
                self.__archivo_servicios,
                self.__archivo_reservas
            ):
                if not ruta.exists():
                    ruta.write_text("[]", encoding="utf-8")

            with open(
                self.__archivo_clientes, "r", encoding="utf-8"
            ) as archivo:
                datos_clientes = json.load(archivo)

            with open(
                self.__archivo_servicios, "r", encoding="utf-8"
            ) as archivo:
                datos_servicios = json.load(archivo)

            with open(
                self.__archivo_reservas, "r", encoding="utf-8"
            ) as archivo:
                datos_reservas = json.load(archivo)

            # Recuperar clientes y validar duplicados

            for datos in datos_clientes:

                cliente = Cliente(
                    datos["identificador"],
                    datos["nombre"],
                    datos["documento"],
                    datos["correo"],
                    datos["telefono"]
                )

                if self.buscar_cliente(cliente.documento):
                    raise DatosInvalidosError(
                        "Hay documentos de clientes duplicados "
                        "en el archivo JSON."
                    )

                if any(
                    c.identificador == cliente.identificador
                    for c in self.__clientes
                ):
                    raise DatosInvalidosError(
                        "Hay identificadores de clientes duplicados "
                        "en el archivo JSON."
                    )

                self.__clientes.append(cliente)

            # Recuperar servicios

            tipos_servicios = {
                "ReservaSalas": ReservaSalas,
                "AlquilerEquipos": AlquilerEquipos,
                "AsesoriaEspecializada": AsesoriaEspecializada
            }

            for datos in datos_servicios:

                tipo = tipos_servicios.get(datos["tipo"])

                if tipo is None:
                    raise DatosInvalidosError(
                        f"Tipo de servicio desconocido: {datos['tipo']}"
                    )

                servicio = tipo(
                    datos["identificador"],
                    datos["nombre"],
                    datos["tarifa"]
                )

                if self.buscar_servicio(servicio.identificador):
                    raise DatosInvalidosError(
                        "Hay identificadores de servicios duplicados "
                        "en el archivo JSON."
                    )

                self.__servicios.append(servicio)

            # Recuperar reservas

            for datos in datos_reservas:

                cliente = self.buscar_cliente(
                    datos["documento_cliente"]
                )

                servicio = self.buscar_servicio(
                    datos["id_servicio"]
                )

                if cliente is None or servicio is None:
                    raise DatosInvalidosError(
                        "No se pudo recuperar una reserva."
                    )

                reserva = Reserva(
                    datos["identificador"],
                    cliente,
                    servicio,
                    datos["cantidad"]
                )

                self.__reservas.append(reserva)

            self.__logger.info(
                "Datos cargados correctamente."
            )

        except (json.JSONDecodeError, KeyError, TypeError) as error:

            self.__logger.error(
                f"Error al cargar los datos: {error}"
            )

            raise DatosInvalidosError(
                "Los archivos JSON contienen datos incorrectos."
            ) from error
