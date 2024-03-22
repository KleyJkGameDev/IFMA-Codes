import java.util.Arrays;

public class Transfer {
    private final String type[] = {"Pix", "Debito", "Credito"};
    
    
    /** 
     * @return String
     */
    @Override
    public String toString() {
        return "Transfer [type=" + Arrays.toString(type) + "]";
    }
    
    
    /** 
     * @return String
     */
    public String getTypePix(){
        return type[0];
    }
    
    /** 
     * @return String
     */
    public String getTypeDebito(){
        return type[1];
    }
    
    /** 
     * @return String
     */
    public String getTypeCredito(){
        return type[2];
    }

}


