
class Data {
    int dia;
    int mes;
    int ano;

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

    String getDataCompleta(){
        String dataStringGet = this.dia+"/"+this.mes+"/"+this.ano;
        return dataStringGet;
    }
}

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

    Conta(){
        Conta.total_contas++;
        this.id_conta += Conta.id_geral;
        Conta.id_geral++;
    }
    
    public static int getTotal_contas() {
        return Conta.total_contas;
    }
    public int getIdentificador() {
        return this.id_conta;
    }
    public String getAgencia() {
        return this.bank.getAgencia();
    }
    public void setAgencia(String agencia) {
        this.bank.setAgencia(agencia);
    }

    public String getData() {
        return this.dataAbertura.getDataCompleta();
    }
    public void setData(int dia, int mes, int ano) {
        this.dataAbertura.setDataCompleta(dia, mes, ano);
    }
    
    public int getNumero() {
        return numero;
    }
    public void setNumero(int numero) {
        this.numero = numero;
    }
    
    double getLimite() {
        return this.limite;
    }
    void setLimite(double limite) {
        this.credito = limite;
        this.limite = limite;
    }

    double getSaldo(){
        return this.saldo;
    }
    double getCredito(){
        return this.credito;
    }

    double getSaldoComLimite(){
        return this.saldo + this.limite;
    }

    boolean setDeposito(double deposito){
        if (deposito>0 && (deposito+this.saldo)<=this.limite) {
            this.saldo += deposito;
            return true;    
        }else{
            return false;
        }
    }

    boolean setSaqueCredito(double valor){
        if (valor>0 && valor<=this.credito) {
            this.credito -= valor;
            return true;
        }else{
            return false;
        }  
    }
    boolean setSaque(double valor){
        if (valor>0 && valor<=this.saldo) {
            this.saldo -= valor;
            return true;
        }else{
            return false;
        }  
    }

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

    public void getTitular() {
        System.out.println("- Nome: "+this.titular.getNome());
        System.out.println("- Sobrenome: "+this.titular.getSobre());
        System.out.println("- CPF: "+this.titular.getCpf());
        System.out.println("- Idade: "+this.titular.getIdade());
    }
    public void setTitularObject(Cliente titular) {
        this.titular = titular;
    }
    public void setTitularString(String nome, String sobre, 
    String cpf, int idade) {
        this.titular.setNome(nome);
        this.titular.setSobre(sobre);
        this.titular.setCpf(cpf);
        this.titular.setIdade(idade);
    }
   
    public void setBankString(String name_bank, int num_bank,
        boolean national, String agencia_bank) {
        this.bank.setName_bank(name_bank);
        this.bank.setNumber_bank(num_bank);
        this.bank.setIs_national(national);
        this.bank.setAgencia(agencia_bank);
    }
    public void setBank(Bank bank) {
        this.bank = bank;
    }

    double getRendimento(){
        return (this.saldo*0.1);
    }
    
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
