
from cliente import Cliente
from servicios import Servicio
from reserva import Reserva
from excepciones import DatosInvalidosError
from logs import obtener_logger


class Gestor:

    def __init__(self):
        self.__clientes = []
        self.__servicios = []
        self.__reservas = []
        self.__logger = obtener_logger()

        self.__logger.info("Sistema iniciado correctamente.")

    def registrar_cliente(self, cliente):

        if not isinstance(cliente, Cliente):
            self.__logger.error("Intento de registro con cliente invalido.")
            raise DatosInvalidosError(
                "El objeto no es un cliente valido."
            )

        if any(c.documento == cliente.documento for c in self.__clientes):
            self.__logger.warning("Documento de cliente duplicado.")
            raise DatosInvalidosError(
                "El cliente ya se encuentra registrado."
            )

        if any(c.identificador == cliente.identificador
               for c in self.__clientes):
            self.__logger.warning("Identificador de cliente duplicado.")
            raise DatosInvalidosError(
                "El identificador del cliente ya existe."
            )

        self.__clientes.append(cliente)

        self.__logger.info(
            f"Cliente registrado: {cliente.nombre}"
        )

    def registrar_servicio(self, servicio):

        if not isinstance(servicio, Servicio):
            self.__logger.error("Intento de registro con servicio invalido.")
            raise DatosInvalidosError(
                "El objeto no es un servicio valido."
            )

        if any(s.identificador == servicio.identificador
               for s in self.__servicios):
            self.__logger.warning("Identificador de servicio duplicado.")
            raise DatosInvalidosError(
                "El servicio ya se encuentra registrado."
            )

        self.__servicios.append(servicio)

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
        servicio = self.buscar_servicio(id_servicio)

        if cliente is None:
            self.__logger.error(
                f"Intento de reserva con cliente inexistente: {documento}"
            )
            raise DatosInvalidosError("El cliente no existe.")

        if servicio is None:
            self.__logger.error(
                f"Intento de reserva con servicio inexistente: {id_servicio}"
            )
            raise DatosInvalidosError("El servicio no existe.")

        if any(r.identificador == identificador
               for r in self.__reservas):
            self.__logger.warning("Identificador de reserva duplicado.")
            raise DatosInvalidosError("La reserva ya existe.")

        reserva = Reserva(
            identificador,
            cliente,
            servicio,
            cantidad
        )

        self.__reservas.append(reserva)

        self.__logger.info(
            f"Reserva creada: {identificador}"
        )

        return reserva

    def listar_clientes(self):
        return list(self.__clientes)

    def listar_servicios(self):
        return list(self.__servicios)

    def listar_reservas(self):
        return list(self.__reservas)
