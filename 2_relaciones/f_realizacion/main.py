from notificadores import *

def main():
    mensaje = "Hola, este es un mensaje importante."

    notificadores_list = [
        EmailNotificador(),
        SMSNotificador(),
        PushNotificador()
    ]

    for notificador in notificadores_list:
        notificador.enviar_notificacion(mensaje)

if __name__ == "__main__":
    main()

"""
! Conceptos Clave

* Realización:
- Es una relación entre una interfaz y una clase concreta.
- La clase concreta provee la implementación de los métodos definidos en la interfaz.
- Las clases EmailNotificador, SMSNotificador y PushNotificador realizan la interfaz Notificador al implementar el método enviar_notificacion().

? Clases Abstractas e Interfaces en Python:
- Python no tiene interfaces como otros lenguajes (por ejemplo, Java), pero podemos usar clases abstractas para lograr un comportamiento similar.
- El módulo abc (Abstract Base Classes) permite definir clases abstractas y métodos abstractos.
- Usamos el módulo abc para definir la clase abstracta Notificador y su método abstracto enviar_notificacion().

TODO: Polimorfismo:
- Al iterar sobre la lista notificadores, podemos llamar al método enviar_notificacion() sin preocuparnos por el tipo específico de notificador, aprovechamos el polimorfismo.
- Cada objeto responde a los métodos según su propia implementación, sin importar el tipo específico de notificador.
"""