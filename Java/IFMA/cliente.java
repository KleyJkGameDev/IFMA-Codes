package Java.IFMA;

public class cliente {
    static class Cliente {
        private String nome;
        private String sobre;
        private String cpf;
        private int idade;

        public String getNome() {
            return this.nome;
        }
        public void setNome(String nome) {
            this.nome = nome;
        }
        public String getSobre() {
            return this.sobre;
        }
        public void setSobre(String sobre) {
            this.sobre = sobre;
        }
        public int getIdade() {
            return idade;
        }
        public void setIdade(int idade) {
            if (idade >= 0) {
                this.idade = idade;
            }else{
                System.out.println("Idade invalida");
                this.idade = -1;
            }  
        }
        public String getCpf() {
            return this.cpf;
        }
        public void setCpf(String cpf) {
            if (validaCPF(cpf)==true && this.idade <=60) {
                this.cpf = cpf;
            }else{
                //System.out.println("CPF Invalido");
                this.cpf = "invalido";
            }
        }
        
        private boolean validaCPF(String CPF){
            if (CPF.length() == 14 || CPF.length() == 11) {
                return true;
            }else{
                return false;
            }
        }

    }
}
