class Carro:
    def __init__(self, marca):
        self.color='rojo'
        self.marca=marca
        self.velocidad=10
        
    def frenar(self):
        self.velocidad=0
    
    def acelerar(self):
        self.velocidad+=10