package br.com.caelum.contas;
import br.com.caelum.javafx.api.util.Evento;

public class ManipuladorDeContas {

    private Conta conta;

    public void criaConta(Evento evento){
        Conta conta = new Conta();
        conta.setAgencia("0001");
        conta.setNumero(1234);
        conta.setTitularString("Kleyton", "Lima", "025.771.673-42", 18);
    }
    public void deposita(Evento evento){
        double valorDigitado = evento.getDouble("valor");
        this.conta.setDeposito(valorDigitado);
    }
}
