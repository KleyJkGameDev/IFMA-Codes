from conta import Conta
from cliente import Cliente
from func import Funcionario

cl1 = Cliente("kleytinn", "025.771.673-42", 18)
cl2 = Cliente("pedro", "025.771.709-00", 20)
cl3 = Cliente("igu", "0932840923", 17)
cl4 = Cliente("david", "12830912830192", 20)
c1 = Conta(cl1, 1001, 1000, 10000)
c2 = Conta(cl2, 1002, 1300, 8000)
c3 = Conta(cl3, 1003, 2342)
c4 = Conta(cl4, 1004, 3242)
c1.toString()
c2.toString()
c3.toString()
c4.toString()

c2.get_totalContas()
