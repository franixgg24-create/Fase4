
from gestor import Gestor
from cliente import Cliente
from servicios import ReservaSalas, AlquilerEquipos, AsesoriaEspecializada
from excepciones import DatosInvalidosError


def mostrar_menu():
    print("\n========== SOFTWARE FJ ==========")
    print("1. Registrar cliente")
    print("2. Registrar servicio")
    print("3. Crear reserva")
    print("4. Consultar clientes")
    print("5. Consultar servicios")
    print("6. Consultar reservas")
    print("0. Salir")
    print("=================================")


def registrar_cliente(gestor):
    identificador = input("Identificador: ")
    nombre = input("Nombre: ")
    documento = input("Documento: ")
    correo = input("Correo electronico: ")
    telefono = input("Telefono: ")

    cliente = Cliente(
        identificador, nombre, documento, correo, telefono
    )

    gestor.registrar_cliente(cliente)
    print("Cliente registrado correctamente.")


def registrar_servicio(gestor):
    print("\nTipo de servicio:")
    print("1. Reserva de salas")
    print("2. Alquiler de equipos")
    print("3. Asesoria especializada")

    opcion = input("Seleccione una opcion: ").strip()

    identificador = input("Identificador del servicio: ")
    nombre = input("Nombre del servicio: ")
    tarifa = float(input("Tarifa del servicio: "))

    if opcion == "1":
        servicio = ReservaSalas(identificador, nombre, tarifa)
    elif opcion == "2":
        servicio = AlquilerEquipos(identificador, nombre, tarifa)
    elif opcion == "3":
        servicio = AsesoriaEspecializada(identificador, nombre, tarifa)
    else:
        print("Opcion no valida.")
        return

    gestor.registrar_servicio(servicio)
    print("Servicio registrado correctamente.")


def crear_reserva(gestor):
    identificador = input("Identificador de la reserva: ")
    documento = input("Documento del cliente: ")
    id_servicio = input("Identificador del servicio: ")
    cantidad = int(input("Cantidad solicitada: "))

    reserva = gestor.crear_reserva(
        identificador, documento, id_servicio, cantidad
    )

    print("\nReserva creada correctamente.")
    print(reserva.mostrar_reserva())


def consultar_clientes(gestor):
    clientes = gestor.listar_clientes()

    if not clientes:
        print("No hay clientes registrados.")
        return

    for cliente in clientes:
        print("\n" + cliente.mostrar_informacion())


def consultar_servicios(gestor):
    servicios = gestor.listar_servicios()

    if not servicios:
        print("No hay servicios registrados.")
        return

    for servicio in servicios:
        print("\n" + servicio.mostrar_informacion())
        print(f"Tarifa: ${servicio.tarifa:,.2f}")


def consultar_reservas(gestor):
    reservas = gestor.listar_reservas()

    if not reservas:
        print("No hay reservas registradas.")
        return

    for reserva in reservas:
        print("\n" + reserva.mostrar_reserva())


def ejecutar():
    gestor = Gestor()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opcion: ")

        try:
            if opcion == "1":
                registrar_cliente(gestor)

            elif opcion == "2":
                registrar_servicio(gestor)

            elif opcion == "3":
                crear_reserva(gestor)

            elif opcion == "4":
                consultar_clientes(gestor)

            elif opcion == "5":
                consultar_servicios(gestor)

            elif opcion == "6":
                consultar_reservas(gestor)

            elif opcion == "0":
                print("Gracias por utilizar Software FJ.")
                break

            else:
                print("Opcion no valida.")

        except (DatosInvalidosError, ValueError) as error:
            print(f"Error: {error}")


if __name__ == "__main__":
    ejecutar()
