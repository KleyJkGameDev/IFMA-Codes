
public class Bank {
    private String name_bank;
    private int number_bank;
    private boolean is_national;
    private String agencia;
    private String type_transf;

    public Bank(String name_bank, int number_bank, boolean is_national) {
        this.name_bank = name_bank;
        this.number_bank = number_bank;
        this.is_national = is_national;
    }
    public Bank(){
        
    }

    @Override
    public String toString() {
        return "Bank [name_bank=" + name_bank + ", number_bank="
         + number_bank + ", is_national=" + is_national + "]";
    }


    public String getAgencia() {
        return agencia;
    }
    public void setAgencia(String agencia) {
        this.agencia = agencia;
    }
    public String getName_bank() {
        return name_bank;
    }
    public int getNumber_bank() {
        return number_bank;
    }
    public boolean isIs_national() {
        return is_national;
    }
    public void setName_bank(String name_bank) {
        this.name_bank = name_bank;
    }
    public void setNumber_bank(int number_bank) {
        this.number_bank = number_bank;
    }
    public void setIs_national(boolean is_national) {
        this.is_national = is_national;
    }
    
    public String getType_transf() {
        return type_transf;
    }
    public void setType_transf(String type_transf) {
        this.type_transf = type_transf;
    }
    
}
