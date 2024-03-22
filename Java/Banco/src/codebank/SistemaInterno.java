package codebank;

public class SistemaInterno {
    
    public String login(Autenticavel a){
        int senha = 1234;
        boolean ok = a.autentica(senha);
        if (ok == true) {
            return "Login realizado com sucesso";
        }else{
            return "Senha incorreta";
        }
    }
}
