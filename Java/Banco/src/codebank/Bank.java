package codebank;
/**
 * Classe responsável por gerenciar dados do Banco
 * @author Kleyton Lima
 */
public class Bank {
    private String name_bank;
    private int number_bank;
    private boolean is_national;
    private String agencia;

    /**
     * Construtor personalizado com 3 parâmetros
     * Preencher previamente name, number e is_national
     * @param String name_bank
     * @param int number_bank
     * @param boolean is_national
     */
    public Bank(String name_bank, int number_bank, boolean is_national) {
        this.name_bank = name_bank;
        this.number_bank = number_bank;
        this.is_national = is_national;
    }
    /**
     * Construtor sem parâmetros - (Padrão)
     */
    public Bank(){
        
    }

    
    /** 
     * Retorna dados do Banco em uma lista
     * @return String
     */
    @Override
    public String toString() {
        return "Bank [name_bank=" + name_bank + ", number_bank="
         + number_bank + ", is_national=" + is_national + "]";
    }
    
    /** 
     * Método que retorna o nome da Agência
     * @return String agencia
     */
    public String getAgencia() {
        return agencia;
    }
    
    /** 
     * Método para settar nome da Agência
     * @param String agencia
     */
    public void setAgencia(String agencia) {
        this.agencia = agencia;
    }
    
    /** 
     * Método que retorna nome do Banco
     * @return String name_bank
     */
    public String getName_bank() {
        return name_bank;
    }

    
    /** 
     * Método que retorna número do Banco
     * @return int
     */
    public int getNumber_bank() {
        return number_bank;
    }

    
    /** 
     * Método que retorna se é ou não nacional
     * @return boolean
     */
    public boolean isIs_national() {
        return is_national;
    }

    
    /** 
     * Método para settar nome do Banco
     * @param String name_bank
     */
    public void setName_bank(String name_bank) {
        this.name_bank = name_bank;
    }

    
    /** 
     * Método para settar número do banco
     * @param int number_bank
     */
    public void setNumber_bank(int number_bank) {
        this.number_bank = number_bank;
    }

    
    /** 
     * Método para settar se é ou não nacional
     * @param boolean is_national
     */
    public void setIs_national(boolean is_national) {
        this.is_national = is_national;
    }
    
}
