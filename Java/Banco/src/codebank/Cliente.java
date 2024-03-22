package codebank;
/**
 * Classe responsável por gerenciar dados do Cliente
 * @author Kleyton Lima
 */
public class Cliente {
    private String nome;
    private String sobre;
    private String cpf;
    private int idade;

    /**
     * Método que retorna nome do titular
     * @return String nome
     */
    public String getNome() {
        return this.nome;
    }
    /**
     * Método para settar nome do titualar
     * @param String nome
     */
    public void setNome(String nome) {
        this.nome = nome;
    }
    /**
     * Método que retorna sobrenome do titular
     * @return String sobrenome
     */
    public String getSobre() {
        return this.sobre;
    }
    /**
     * Método para settar sobrenome do titular
     * @param String sobrenome
     */
    public void setSobre(String sobre) {
        this.sobre = sobre;
    }
    /**
     * Método que retorna idade do titular
     * @return int idade
     */
    public int getIdade() {
        return idade;
    }
    /**
     * Método para settar idade do titular
     * (se idade não for válida, idade = -1)
     * @param int idade
     */
    public void setIdade(int idade) {
        if (idade >= 0) {
            this.idade = idade;
        }else{
            System.out.println("Idade invalida");
            this.idade = -1;
        }  
    }
    /**
     * Método que retorna CPF do titular
     * @return String cpf
     */
    public String getCpf() {
        return this.cpf;
    }
    /**
     * Método para settar cpf do titular
     * @param String cpf
     */
    public void setCpf(String cpf) {
        if (validaCPF(cpf)==true && this.idade <=60) {
            this.cpf = cpf;
        }else{
            //System.out.println("CPF Invalido");
            this.cpf = "invalido";
        }
    }
    /**
     * Método para validar cpf do titular
     * @param String cpf
     * @return boolean "true" se for validado
     * @return boolean "false" se não for validado
     */
    private boolean validaCPF(String CPF){
        if (CPF.length() == 14 || CPF.length() == 11) {
            return true;
        }else{
            return false;
        }
    }
}
