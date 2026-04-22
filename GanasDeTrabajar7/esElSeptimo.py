import time

class Nodo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.conexiones = []
    
    def agregarConexion(self, nodo):
        self.conexiones.append(nodo)
    
    def enviarMensaje(self, mensaje):
        print(f"{self.nombre} envia {mensaje}")
        for conexion in self.conexiones:
            conexion.recibirMensaje(mensaje)
    
    def recibirMensaje(self, mensaje):
        print(f"{self.nombre} envia: {mensaje}")
    
    def eliminarConexion(self, nodo):
        self.conexiones.remove(nodo)

servidor = Nodo("Servidor")
cliente1 = Nodo("Cliente 1")
cliente2 = Nodo("Cliente 2")
cliente3 = Nodo("Cliente 3")
enrutamiento = Nodo("Enrutamiento")

servidor.agregarConexion(cliente1)
servidor.agregarConexion(cliente2)
servidor.agregarConexion(cliente3)
servidor.agregarConexion(enrutamiento)
cliente1.agregarConexion(servidor)
cliente2.agregarConexion(servidor)
cliente3.agregarConexion(servidor)
enrutamiento.agregarConexion(servidor)

servidor.enviarMensaje("Hola a todos")

print("Simulando desconexión y reconexión dinámica...")
enrutamiento.eliminarConexion(servidor)
time.sleep(3)
enrutamiento.agregarConexion(servidor)
print("Hola de nuevo a todos")