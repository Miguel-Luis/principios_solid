from usuario import Usuario

def main():
    usuario = Usuario("Juan Pérez", "juan@example.com")
    usuario.guardar_en_bd()
    usuario.enviar_email("Bienvenido a nuestra plataforma.")

if __name__ == "__main__":
    main()
