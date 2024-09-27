import smtplib

class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email

    def guardar_en_bd(self):
        # Simulación de guardar en base de datos
        print(f"Guardando el usuario {self.nombre} en la base de datos.")

    def enviar_email(self, mensaje):
        # Simulación de envío de correo electrónico
        print(f"Enviando email a {self.email} con el mensaje: {mensaje}")
        # Código real podría usar smtplib para enviar correos
