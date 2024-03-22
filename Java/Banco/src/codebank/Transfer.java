package codebank;
import java.util.Arrays;

/**
 * Classe responsável por gerenciar tipo de Transferência
 */

public class Transfer {
    private final String type[] = {"Pix", "Debito", "Credito"};
    
    
    /** 
     * Método que retorna lista em texto
     * @return String type_transferencia
     */
    @Override
    public String toString() {
        return "Transfer [type=" + Arrays.toString(type) + "]";
    }
    
    
    /** 
     * Método que retorna o tipo PIX
     * @return String type[0]
     */
    public String getTypePix(){
        return type[0];
    }
    
    /** 
     * Método que retorna o tipo DEBITO
     * @return String type[1]
     */
    public String getTypeDebito(){
        return type[1];
    }
    
    /** 
     * Método que retorna o tipo CREDITO
     * @return String type[2]
     */
    public String getTypeCredito(){
        return type[2];
    }

}


