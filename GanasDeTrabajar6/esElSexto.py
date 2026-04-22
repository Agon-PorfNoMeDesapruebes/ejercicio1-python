class Actividad:
    def __init__(self, nombre, id):
        self.nombre = nombre
        self.id = id
        self.almacenamientoMensajes = []  # Para el servidor almacenar mensajes
    
    def enviarMensaje(self, mensaje, dueñoId):
        # Las computadoras envían mensajes al servidor
        if self.id != "123456789":  # Si no es el servidor
            servidor.Comunicacion(mensaje, self.id, dueñoId)
    
    def Comunicacion(self, mensaje, receptorId, dueñoId):
        # El servidor recibe mensajes
        if self.id == "123456789":
            self.almacenamientoMensajes.append((mensaje, receptorId, dueñoId))
            self.solicitud()
    
    def solicitud(self):
        # El servidor decide si transmitir
        if self.almacenamientoMensajes:
            mensaje, remitente, destinatario = self.almacenamientoMensajes.pop(0)
            if {remitente} != {destinatario}:
                consultar = input(f"¿Desea pasar el mensaje '{mensaje}' de {remitente} a {destinatario}?, si, no: ")
                if consultar.lower() == "si":
                    print(f"Mensaje transmitido: '{mensaje}' de {remitente} a {destinatario}")
                    # Aquí podrías agregar lógica para enviar al destinatario real
                else:
                    print("Mensaje rechazado.")
            else:
                print("No puedes mandarte mensajes a ti mismo")
        else:
            print("No hay mensajes pendientes.")
                

servidor = Actividad("Servidor", "123456789")
compu1 = Actividad("Computadora1", "1")
compu2 = Actividad("Computadora2", "2")
compu3 = Actividad("Computadora3", "3")

compu1.enviarMensaje("Hola Ari", "2") 