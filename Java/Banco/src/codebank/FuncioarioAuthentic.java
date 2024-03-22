package codebank;

public abstract class FuncioarioAuthentic extends Funcionario {

    private int senha = 1234;

    public boolean autentica(int senha){
        if (this.senha == senha) {
            System.out.println("Login realizado");
            return true;
        }else{
            System.out.println("Acesso Negado");
            System.out.println("teste");
            return false;
        }
    }

    @Override
    public double getBonifica() {
        return 0;
    }
}
