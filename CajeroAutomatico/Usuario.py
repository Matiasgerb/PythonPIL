class Usuario:
    def __init__(self,usuario,contrasenia):
        self.usuario = usuario 
        self.contrasenia = contrasenia

    def getUsuario(self):
        self.usuario

    def getContrasenia(self):
        self.contrasenia = '1234'

us1 = Usuario('admin','1234')
        
print(f'us1 -> {us1.usuario}, {us1.contrasenia}')