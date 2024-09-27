from usuario import Usuario
from usuario_repositorio import UsuarioRepositorio
from servicio_email import ServicioEmail

def main():
    usuario = Usuario("Juan Pérez", "juan@example.com")

    # Crear instancias de los servicios
    repositorio = UsuarioRepositorio()
    servicio_email = ServicioEmail()

    # Utilizar los servicios
    repositorio.guardar(usuario)
    servicio_email.enviar_email(usuario.email, "Bienvenido a nuestra plataforma.")

if __name__ == "__main__":
    main()
