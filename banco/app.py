from conta import Conta

c = Conta("Jimmy", 20, "Masculino", "Nubank")
c.abrirConta(2000, 0) 
c.depositar(500.50)
c.sacar(560)
print(c.__str__())
c.depositar(2.55)
c.saldo()
c.sacar(233.50)
c.saldo()
c.fecharConta()