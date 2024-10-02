from notificador import Notificador

class EmailNotificador(Notificador):
    def enviar_notificacion(self, mensaje):
        print(f"Enviando notificación por Email: {mensaje}")
