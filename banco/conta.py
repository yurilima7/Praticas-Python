from acoes_banco import AcoesBanco
from cliente import Cliente

class Conta(Cliente, AcoesBanco):
    def __init__(self, nome, idade, sexo, nomeBanco):
        super().__init__(nome, idade, sexo)
        self.__nomeBanco = nomeBanco
        self.__aberta = False
        self.__conta = 0
        self.__saldo = 0.0
        self.__digito = 0

    def getConta(self):
        return self.__conta
    
    def setConta(self, conta):
        self.__conta = conta

    def getDigito(self):
        return self.__digito
    
    def setDigito(self, digito):
        self.__digito = digito

    def getNomeBanco(self):
        return self.__nomeBanco
    
    def setNomeBanco(self, nomeBanco):
        self.__nomeBanco = nomeBanco

    def getSaldo(self):
        return self.__saldo

    def setSaldo(self, saldo):
        self.__saldo = saldo 

    def isAberta(self):
        return self.__aberta

    def setAberta(self, aberta):
        self.__aberta = aberta  
        
    def abrirConta(self, numero, digito):
        if(self.isAberta()):
            print("Conta já está aberta!")
        else:
            self.setAberta(True)
            self.setConta(numero)
            self.setDigito(digito)
            print("Conta aberta com sucesso!")
            self.setSaldo(0.0)

    def fecharConta(self):
        if(self.isAberta() == False):
            print("Impossivel encerrar conta que não esta aberta!")
        else:
            if(self.getSaldo() == 0):
                self.setAberta(False)
                print("Conta encerrada com sucesso!")
            elif(self.getSaldo() < 0):
                print("Impossivel encerrar conta, pois cliente está em debito com o banco!")
            else:
                print("Impossivel encerrar conta, pois ha saldo na mesma!")

    def sacar(self, valor):
        pass
    
    def depositar(self, valor):
        pass

    def saldo(self):
        pass