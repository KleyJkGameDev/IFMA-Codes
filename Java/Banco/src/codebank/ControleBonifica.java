package codebank;

public class ControleBonifica {
    private double total_bonifica = 0;

    public void registra(Funcionario funcionario){
        System.out.println("Adicionando bonificação do funcionario ("
        +funcionario+"): "+funcionario.getNome()+" no valor de: R$"
        +funcionario.getBonifica());
        this.total_bonifica += funcionario.getBonifica();
    }

    public double getTotal_bonifica() {
        return this.total_bonifica;
    }
}
