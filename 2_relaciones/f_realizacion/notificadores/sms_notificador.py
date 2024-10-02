from notificador import Notificador

class SMSNotificador(Notificador):
    def enviar_notificacion(self, mensaje):
        print(f"Enviando notificación por SMS: {mensaje}")
