
# PROYECTO: SOFTWARE FJ
# ARCHIVO: excepciones.py
# DESCRIPCION: Manejo de excepciones personalizadas


class ErrorSistema(Exception):
    """Representa un error general del sistema."""
    pass


class DatosInvalidosError(ErrorSistema):
    """Se produce cuando los datos no cumplen las validaciones."""
    pass


class ClienteNoEncontradoError(ErrorSistema):
    """Se produce cuando un cliente no existe."""
    pass

class ServicioNoDisponibleError(ErrorSistema):
    """Se produce cuando un servicio no puede utilizarse."""
    pass


class ReservaInvalidaError(ErrorSistema):
    """Se produce cuando una reserva no cumple las condiciones."""
    pass

class OperacionNoPermitidaError(ErrorSistema):
    """Se produce cuando una operacion no esta permitida."""
    pass
