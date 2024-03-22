package codebank;

public class ContaPoupanca extends Conta{
    //private String type_conta;
    @Override
    public String getTipoConta() {
        //this.type_conta = tipo_conta[0];
        return tipo_conta[0];
    }
}

/**
 * ContaCorrente
 */
class ContaCorrente extends Conta{

    @Override
    public String getTipoConta() {
        return tipo_conta[1];
    }
    
}
