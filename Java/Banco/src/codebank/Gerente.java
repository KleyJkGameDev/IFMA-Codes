package codebank;

public class Gerente extends Funcionario implements Autenticavel{
    protected int senha = 1234;
    //private int numeroDeFuncionariosGerenciados;

    public boolean autentica(int senha){
        if (this.senha == senha) {
            System.out.println("Acesso Permitido Gerente");
            return true;
        }else{
            System.out.println("Acesso Negado");
            return false;
        }
    }

    public int getSenha() {
        return senha;
    }

    public void setSenha(int senha) {
        this.senha = senha;
    }

    public void imprimeDados(){
        System.out.println("Nome: "+this.getNome());
        System.out.println("CPF: "+this.getCpf());
        System.out.println("Salario: "+this.getSalario());
        System.out.println("Senha: "+this.getSenha());
    }
    @Override
    public double getBonifica() {
        //return super.getBonifica() + 100
        return this.salario*1.4+1000.0;
    }
    public int getNumeroDeFuncionariosGerenciados() {
        return total_funcionarios;
    }
}

/**
 * Class Diretor
 */
class Diretor extends Funcionario implements Autenticavel{

    protected int senha = 1234;

    public boolean autentica(int senha){
        if (this.senha == senha) {
            System.out.println("Acesso Permitido Diretor");
            return true;
        }else{
            System.out.println("Acesso Negado");
            return false;
        }
    }

    public void imprimeDados(){
        System.out.println("Nome: "+this.getNome());
        System.out.println("CPF: "+this.getCpf());
        System.out.println("Salario: "+this.getSalario());
        System.out.println("Senha: "+this.getSenha());
    }
    @Override
    public double getBonifica() {
        return this.salario*2.0+1000.00;
    }
    public int getSenha() {
        return senha;
    }
    public void setSenha(int senha) {
        this.senha = senha;
    }
    
}
