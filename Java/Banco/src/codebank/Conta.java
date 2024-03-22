package codebank;
/**
 * Classe responsável por gerenciar Data
 */
class Data {
    int dia;
    int mes;
    int ano;

    
    /** 
     * Método para settar data completa
     * @param dia
     * @param mes
     * @param ano
     */
    void setDataCompleta(int dia, int mes, int ano){
        if (dia >=1 && dia <=31) {
            this.dia = dia;
            if (mes >= 1 && mes <= 12) {
                this.mes = mes;
                if (ano >= 1000 && ano <= 9999) {
                    this.ano = ano;
                }
            }    
        }else{
            System.out.println("Data invalida");
            this.ano = 0;
            this.dia = 0;
            this.mes = 0;
        }
    }

    
    /** 
     * Método que retorna data formatada
     * @return String dataStringGet
     */
    String getDataCompleta(){
        String dataStringGet = this.dia+"/"+this.mes+"/"+this.ano;
        return dataStringGet;
    }
}

/**
 * Classe que Gerencia a Conta
 */

public class Conta {
    private int numero;
    //private Bank banco;
    private Bank bank = new Bank();
    private Data dataAbertura = new Data();
    private Cliente titular = new Cliente();
    private double saldo;
    private double credito;
    private double limite;
    private static int id_geral = 1001;
    int id_conta;
    private static int total_contas;

    /**
     * Construtor sem parâmetros - (Padrão)
     * atributo global (total_contas) soma +1 sempre que instanciado
     * ao ser chamado, objeto recebe ele mesmo mais valor 
     * de suporte para geração de númeração única por objeto criado
     */
    public Conta(){
        Conta.total_contas++;
        this.id_conta += Conta.id_geral;
        Conta.id_geral++;
    }
    /**
     * Método que retorna total de contas
     * @return int total_contas
     */
    public static int getTotal_contas() {
        return Conta.total_contas;
    }
    /**
     * Método que retorna ID da conta
     * @return int id_conta
     */
    public int getIdentificador() {
        return this.id_conta;
    }
    /**
     * Método que retorna agência > Class.Bank
     * @return String agencia
     */
    public String getAgencia() {
        return this.bank.getAgencia();
    }
    /**
     * Método para settar agencia > Class.Bank
     * @param String agencia
     */
    public void setAgencia(String agencia) {
        this.bank.setAgencia(agencia);
    }
    /**
     * Método que retorna data formatada > Class.Data
     * @return String dataAbertura
     */
    public String getData() {
        return this.dataAbertura.getDataCompleta();
    }
    /**
     * Método para settar data completa
     * @param int dia
     * @param int mes
     * @param int ano
     */
    public void setData(int dia, int mes, int ano) {
        this.dataAbertura.setDataCompleta(dia, mes, ano);
    }
    /**
     * Método que retorna numero da conta
     * @return int numero
     */
    public int getNumero() {
        return numero;
    }
    /**
     * Método para settar numero
     * @param int numero
     */
    public void setNumero(int numero) {
        this.numero = numero;
    }
    /**
     * Método que retorna limite da conta
     * @return double limite
     */
    double getLimite() {
        return this.limite;
    }
    /**
     * Método para settar limite da conta
     * (settar apenas uma vez e também setta 
     * o crédito atual)
     * @param double limite
     */
    void setLimite(double limite) {
        this.credito = limite;
        this.limite = limite;
    }
    /**
     * Método que retorna saldo
     * @return double saldo
     */
    double getSaldo(){
        return this.saldo;
    }
    /**
     * Método que retorna o cŕedito disponível
     * @return double credito
     */
    double getCredito(){
        return this.credito;
    }
    /**
     * Método que retorna saldo com limite
     * @return double saldo + limite
     */
    double getSaldoComLimite(){
        return this.saldo + this.limite;
    }
    /**
     * Método para fazer depósito na conta atual
     * @param double deposito
     * @return boolean "true" se depósito realizado com sucesso
     * @return boolean "false" se falhar
     */
    boolean setDeposito(double deposito){
        if (deposito>0 && (deposito+this.saldo)<=this.limite) {
            this.saldo += deposito;
            return true;    
        }else{
            return false;
        }
    }
    /**
     * Método para fazer saque na conta atual - (CRÉDITO)
     * @param double valor
     * @return boolean "true" se saque no crédito realizado com sucesso
     * @return boolean "false" se falhar
     */
    boolean setSaqueCredito(double valor){
        if (valor>0 && valor<=this.credito) {
            this.credito -= valor;
            return true;
        }else{
            return false;
        }  
    }
    /**
     * Método para fazer saque na conta atual - (DÉBITO)
     * @param double valor
     * @return boolean "true" se saque realizado com sucesso
     * @return boolean "false" se falhar
     */
    boolean setSaque(double valor){
        if (valor>0 && valor<=this.saldo) {
            this.saldo -= valor;
            return true;
        }else{
            return false;
        }  
    }
    /**
     * Método que transfere saldo entre contas - (DÉBITO)
     * @param Conta destino
     * @param double t_valor
     * @return boolean "true" se transferência for feita com sucesso
     * @return boolean "false" se não for possível transferir
     */
    boolean transfere(Conta destino, double t_valor){
        boolean retirou = this.setSaque(t_valor);
        if (retirou) {
            destino.setDeposito(t_valor);
            System.out.println("Tranferencia realizada com sucesso");
            return true;
        }else{
            System.out.println("Nao foi possivel transferir");
            return false;
        }
    }
    /**
     * Método que retorna titular completo > Class.Cliente
     * @return String Nome
     * @return String Sobrenome
     * @return String CPF
     * @return int idade
     */
    public void getTitular() {
        System.out.println("- Nome: "+this.titular.getNome());
        System.out.println("- Sobrenome: "+this.titular.getSobre());
        System.out.println("- CPF: "+this.titular.getCpf());
        System.out.println("- Idade: "+this.titular.getIdade());
    }
    /**
     * Método para settar titular através de um Object - (Cliente)
     * > Class.Cliente
     * @param Cliente titular
     */
    public void setTitularObject(Cliente titular) {
        this.titular = titular;
    }
    /**
     * Método para settar cada campo do titular através de String > Class.Cliente
     * @param String nome
     * @param String sobrenome
     * @param String CPF
     * @param int idade
     */
    public void setTitularString(String nome, String sobre, 
    String cpf, int idade) {
        this.titular.setNome(nome);
        this.titular.setSobre(sobre);
        this.titular.setCpf(cpf);
        this.titular.setIdade(idade);
    }
    /**
     * Método para settar dados do Banco > Class.Bank
     * @param String name_bank
     * @param int num_bank
     * @param boolean national
     * @param String agencia_bank
     */
    public void setBankString(String name_bank, int num_bank,
        boolean national, String agencia_bank) {
        this.bank.setName_bank(name_bank);
        this.bank.setNumber_bank(num_bank);
        this.bank.setIs_national(national);
        this.bank.setAgencia(agencia_bank);
    }
    /**
     * Método para settar dados do banco através de objeto - (Bank)
     * > Class.Bank
     * @return
     */
    public void setBank(Bank bank) {
        this.bank = bank;
    }
    /**
     * Método que retorna rendimento da conta
     * @return double 10% do saldo
     */
    double getRendimento(){
        return (this.saldo*0.1);
    }
    /**
     * Método para imprimir todos os dados de:
     * - Cliente, Conta e Banco.
     * (retorna mensagem de erro se algum campo estiver vazio)
     * @return String todos_os_dados
     */
    void getImprimaDados(){
        if (checkNull() == true) {
            System.out.println("---> DADOS DO CLIENTE <---");
            System.out.println("#Titular:");
            System.out.println(" - Nome: "+this.titular.getNome());
            System.out.println(" - Sobrenome: "+this.titular.getSobre());
            System.out.println(" - CPF: "+this.titular.getCpf());
            System.out.println(" - Idade: "+this.titular.getIdade());
            System.out.println("#BANCO: ");
            System.out.println(" - Nome: "+this.bank.getName_bank());
            System.out.println(" - Numero: "+this.bank.getNumber_bank());
            System.out.println(" - Agencia: "+this.bank.getAgencia());
            System.out.println(" - Tipo: "+this.bank.isIs_national());
            System.out.println("#CONTA:");
            System.out.println(" - ID: "+this.id_conta);
            System.out.println(" - Data: "+this.getData());
            System.out.println(" - Limite da conta: "+this.limite);
            System.out.println(" - Saldo da Conta: "+this.saldo);
            getTitular();
        }else{
            System.out.println("Algum dos campos nao foi prenchido");
        }
        
    }
    /**
     * Método para checar se existe campo não preenchido
     * @return boolean "true" se for validado
     * @return boolean "false" se não for validado
     */
    boolean checkNull(){
        if (this.titular.getNome() == null || this.titular.getCpf() == null ||
        this.titular.getIdade() == 0 ||this.titular.getSobre() == null) {
            System.out.println("Campos do titular não foram preenchidos");

            if (this.bank.getAgencia()==null||this.bank.getName_bank()==null||
            this.bank.getNumber_bank()==0) {
                System.out.println("Campos do Banco não preenchidos");

                if (this.dataAbertura.getDataCompleta()=="0/0/0"||this.dataAbertura.mes==0||
                this.dataAbertura.ano==0||this.limite==0) {
                    System.out.println("Campos da conta não preenchidos");
                    return false;
                }else{
                    System.out.println("Conta passou");
                }

                return false;
            }else{
                System.out.println("Banco passou");
            }

            return false;
        }else{
            System.out.println("titular passou");
            return true;
        }
    }

}
