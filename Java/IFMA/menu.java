package Java.IFMA;

import Java.IFMA.conta.Conta;

public class menu {
    public static void main(String[] args) {
        //Conta c1 = new Conta("Kleytinn", "025.771.673-42");
        //Conta c2 = new Conta("Jonas", "001.001.173-09");
        Conta c1 = new Conta();
        Conta c2 = new Conta();
        //Cliente clt1 = new Cliente();
        //c1.setTitularObject(clt1);
        c1.setTitularString("Kley", "Lima", "XXX.XXX.XXX-X", 18);
        c2.setTitularString("Jonas", "Grey", "XXX.XXX.XXX-XX", 18);
        c1.setLimite(1000);
        c2.setLimite(1000);

        c1.setDeposito(100);
        c2.setDeposito(100);
        c2.transfere(c1, 100);
        System.out.println("conta1: R$"+c1.getSaldo());
        System.out.println("conta2: R$"+c2.getSaldo());
        //c1.setTitularObject(clt1);
        System.out.println("Rendimento: R$"+c2.getRendimento());
        //c1.setData(10, 12, 2005);
        c1.getImprimaDados();
        //c2.getImprimaDados();
        //System.out.println(Conta.getTotal_contas());
        //System.out.println(c2.getIdentificador());
    }
}
