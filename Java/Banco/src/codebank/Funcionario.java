package codebank;

public class Funcionario {
    protected String nome;
    protected String cpf;
    protected double salario;
    protected static int total_funcionarios;
    
    Funcionario(){
        total_funcionarios++;
    }

    public String getCpf() {
        return cpf;
    }
    public void setCpf(String cpf) {
        this.cpf = cpf;
    }
    public String getNome() {
        return nome;
    }
    public void setNome(String nome) {
        this.nome = nome;
    }
    public double getSalario() {
        return salario;
    }
    public void setSalario(double salario) {
        this.salario = salario;
    }
    public double getBonifica(){
        return this.salario*0.10;
    }
}
