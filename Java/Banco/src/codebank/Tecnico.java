package codebank;

public class Tecnico extends Funcionario{

    @Override
    public double getBonifica() {
        return this.salario*0.2+1000.0;
    }

    public void imprimeDados(){
        System.out.println("Nome: "+this.getNome());
        System.out.println("CPF: "+this.getCpf());
        System.out.println("Salario: "+this.getSalario());
    }
}
