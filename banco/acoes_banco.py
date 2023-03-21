from abc import ABC, abstractmethod

class AcoesBanco(ABC):
    @abstractmethod
    def abrirConta(self, numero, digito):
        pass

    @abstractmethod
    def fecharConta(self):
        pass
    
    @abstractmethod
    def sacar(self, valor):
        pass
    
    @abstractmethod
    def depositar(self, valor):
        pass

    @abstractmethod
    def saldo(self):
        pass