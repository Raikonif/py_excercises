# Exercise 2: Bank Account Class
# Create a class called BankAccount to represent a basic bank account.
# It should have attributes like account_number and balance. Add methods to deposit, withdraw, and display the account balance.
class BankAccount:
    monto = 1000
    print("Bienvenido Banco Alarint.Bo")
    def options(self):
        self.option = int(input("Ingrese que quiere hacer:\n1=Saldo\n2=Depositar\n3=Retirar\n4=Salir\n"))
        self.control = 0
        while self.control== 0:
            if self.option == 1:
                self.balance()
            elif self.option == 2:
                self.depositar()
            elif sel.option == 3:
                self.retirar()
            elif sel.option == 4:
                self.control == 1
                self.salir()
            else:
                print("Error")
                self.options()
    def balance (self):
        print("Su balance es:", self.monto)
        print("Desea hacer otra operacion?:")
        self.options()

    def depositar(self,cantidad):
        self.dep = input("Ingrese el monto a depositar:\n")
        self.monto = self.monto + self.dep
        self.balance()
    
    def retirar(self, cantidad):
        self.retiro = int(input("Ingrese el monto a retirar:\n"))
        self.control = 0
        while self.control == 0:
            if self.retiro > self.monto:
                print("No tiene suficientes fondos para retirar, intente nuevamente")
                self.retiro = int(input("Ingrese monto a retirar:"))
            elif self.retiro <= self.monto:
                self.monto= self.monto - self.retiro
                self.control = 1
                print("Cantidad retirada:", self.retiro)
                self.balance()
    
    def salir(self):
        print("Gracias por usar nuestros servicios")
    
ejecucion = BankAccount()
ejecucion.options()