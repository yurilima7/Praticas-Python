from abc import ABC, abstractmethod

class Cliente(ABC):
    @abstractmethod
    def __init__(self, nome, idade, sexo):
        self.__nome = nome
        self.__idade = idade
        self.__sexo = sexo

    def getNome(self):
        return self.__nome
        
    def setNome(self, nome):
        self.__nome = nome
    
    def getIdade(self):
        return self.__idade
    
    def getSexo(self):
        return self.__sexo
        
    def setSexo(self, sexo):
        self.__sexo = sexo
    
    def setIdade(self, idade):
        self.__idade = idade

    def __str__(self):
        return f"\nnome do cliente: {self.getNome()}\nidade: {self.getIdade()}\nsexo: {self.getSexo()}\n"