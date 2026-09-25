class Paciente:
    
    PREVISIONES: set[str] = {"Fonasa", "Isapre", "Otro"}
    
    def __init__(self, rut:str, nombre:str, edad:int, prevision:str):
        self.rut = rut
        self.edad = edad
        self.nombre = nombre
        self.prevision = prevision

    @property
    def rut(self)->str:
        return self._rut

    @rut.setter
    def rut(self, rut:str)->None:
        self._rut = rut

    @property
    def nombre(self)->str:
            return self._nombre
    
    @nombre.setter
    def nombre(self, nombre:str)->None:
            self._nombre = nombre

    @property
    def edad(self)->int:
            return self._edad
    
    @edad.setter
    def edad(self, edad:str)->None:
            self._edad = edad

    @property
    def prevision(self)->str:
            return self._prevision

    @rut.setter
    def prevision(self, prevision:str)->None:
            self._prevision = str

    def __str__(self)->str:
          return f"""Informacion del paciente\nRUT: {self.rut}\nNombre: {self.nombre}\nEdad: {self.edad}\nPrevision: {self.prevision}"""

    def __repr__(self)->str:
              return f"""Paciente(rut={self.rut}, nombre= {self.nombre}, edad= {self.edad}, prevision= {self.prevision})"""
        

    