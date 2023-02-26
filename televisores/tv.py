class TV:
    numTV=0
    def __init__(self, marca, estado):
        self.marca=marca
        self.estado=estado
        self.canal=1
        self.volumen=1
        self.precio=500
        self.numTV+=1

    def getNumTV(self):
        return self.numTV
    
    @staticmethod
    def setNumTV(num):
        numTV=num
    

    def getMarca(self):
        return self.marca
    
    def setMarca(self, marca):
        self.marca=marca
    
    def getControl(self):
        return self.control

    def setControl(self, control):
        self.control=control
    
    def getVolumen(self):
        return self.volumen
    
    def setVolumen(self, volumen):
        if (self.estado and (volumen<=7 and volumen>=0)):
          self.volumen=volumen
    
    def getCanal(self):
        return self.canal
    
    def setCanal(self, canal):
        if (self.estado and (canal<=120 and canal>=1)):
            self.canal=canal

    def turnOn(self):
        self.estado=True

    def turnOff(self):
        self.estado=False

    def getEstado(self):
        return self.estado
    
    def canalUp(self):
        if (self.estado and self.canal<=119):
            self.canal+=1
            
    def canalDown(self):
        if (self.estado and self.canal>=2):
            self.canal-=1

    def volumenUp(self):
        if (self.estado and self.volumen<=6):
            self.volumen+=1

    def volumenDown(self):
        if(self.estado and self.volumen>=1):
            self.volumen-=1
    
    def getPrecio(self):
        return self.precio
    
    def setPrecio(self, precio):
        self.precio = precio
        
      