package codebank;

/**
 * Classe responsável por gerenciar outras classes
 * @author Kleyton Lima
 * @version 1.0.0
 * @apiNote Não completo
 */
public class App {
    
    /** 
     * Classe Responsável por executar o código no geral
     * @param args
     * @author Kleyton Lima
     * @throws Exception
     */
    public static void main(String[] args) throws Exception {
        // Conta c1 = new Conta("Kleytinn", "025.771.673-42");
        // Conta c2 = new Conta("Jonas", "001.001.173-09");
        ContaCorrente c1 = new ContaCorrente();
        ContaCorrente c2 = new ContaCorrente();
        // Cliente clt1 = new Cliente();
        // Java.IFMA.cliente.Cliente tesCliente = new Java.IFMA.cliente.Cliente();
        // c1.setTitularObject(clt1);
        c1.setTitularString("Kley", "Lima", "XXX.XXX.XXX-XX", 18);
        // c1.setData(12, 1, 2022);
        c1.setBankString("Inter", 1234, false, "0001");
        c2.setTitularString("Jonas", "Grey", "XXX.XXX.XXX-XX", 18);
        c2.setData(25, 11, 2024);
        c2.setBankString("Nubank", 4321, true, "0004");
        c1.setLimite(10000.0);
        c2.setLimite(10000.0);

        c1.setDeposito(1000.0);
        c2.setDeposito(1000.0);
        c2.transfere(c1, 100.0);
        System.out.println("Saldo 1: R$" + c1.getSaldo());
        System.out.println("Saldo 2: R$" + c2.getSaldo());
        // c1.setTitularObject(clt1);
        System.out.println("Rendimento Conta 2: R$" + c2.getRendimento());
        // c1.setData(10, 12, 2005);
        // c1.getImprimaDados();
        // c2.getImprimaDados();
        // System.out.println(Conta.getTotal_contas());
        // System.out.println(c2.getIdentificador());
        // Bank bank = new Bank("Inter",
        // 10001001, false);
        // System.out.println("Nome: "+bank.getName_bank());
        // System.out.println("Numero: "+bank.getNumber_bank());
        // if (bank.isIs_national()) { 
        // System.out.println("Banco Nacional");
        // }else{
            
        // System.out.println("Banco Internacional");
        // }
        // System.out.println(bank.toString());
        // Bank b = new Bank();
        // b.setName_bank("novo banco");
        // c1.setCredito(10500.00);
        System.out.println("Credito 1: " + c1.getCredito());
        c1.setSaqueCredito(400.0);
        System.out.println("Credito 1: " + c1.getCredito());
        System.out.println("Saldo 1: R$" + c1.getSaldo());
        c1.getImprimaDados();
        Gerente gerente = new Gerente();
        Tecnico teste = new Tecnico();
        Diretor func1 = new Diretor();
        ControleBonifica cb = new ControleBonifica();
        teste.setSalario(1000);
        teste.setNome("Kleytinn");
        gerente.setSalario(1000);
        gerente.setNome("Jonas");
        func1.setSalario(1000);
        func1.setNome("Crys");
        cb.registra(gerente);
        cb.registra(func1);
        cb.registra(teste);
        System.out.println(cb.getTotal_bonifica());
        System.out.println(c1.getTipoConta());
        Autenticavel g = new Diretor();
        //g.autentica(1234);
        SistemaInterno si = new SistemaInterno();
        si.login(g);
    }
}
