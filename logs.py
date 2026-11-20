
import logging
from pathlib import Path


def obtener_logger(nombre="SoftwareFJ"):

    ruta_registros = Path(__file__).resolve().parent / "registros"
    ruta_registros.mkdir(exist_ok=True)

    ruta_archivo = ruta_registros / "sistema.log"

    logger = logging.getLogger(nombre)
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        archivo = logging.FileHandler(
            ruta_archivo,
            encoding="utf-8"
        )

        formato = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(message)s"
        )

        archivo.setFormatter(formato)
        logger.addHandler(archivo)

    return logger
