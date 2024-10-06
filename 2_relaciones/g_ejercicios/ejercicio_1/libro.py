class Libro:
    def __init__(self, titulo):
        self.titulo = titulo
        self._disponible = True
        
    def prestar(self):
        if self._disponible:
            self._disponible = False
            return True
        
        return False
    
    def devolver(self):
        self._disponible = True
