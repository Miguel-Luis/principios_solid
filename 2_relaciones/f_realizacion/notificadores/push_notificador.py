from notificador import Notificador

class PushNotificador(Notificador):
    def enviar_notificacion(self, mensaje):
        print(f"Enviando notificación Push: {mensaje}")
