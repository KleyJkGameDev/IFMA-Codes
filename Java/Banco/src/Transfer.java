import java.util.Arrays;

public class Transfer {
    private final String type[] = {"Pix", "Debito", "Credito"};
    
    @Override
    public String toString() {
        return "Transfer [type=" + Arrays.toString(type) + "]";
    }
    
    public String getTypePix(){
        return type[0];
    }
    public String getTypeDebito(){
        return type[1];
    }
    public String getTypeCredito(){
        return type[2];
    }

}
