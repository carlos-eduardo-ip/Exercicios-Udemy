package entities;

public class Bank {
    private String name;
    private int accNumber;
    private double balance;

    public String toString(){
        return "\nAccount "
                + accNumber
                + ", Holder: "
                + getName()
                + ", Balance: $ "
                + String.format("%.2f",balance);
    }
    public Bank(String name, int accNumber, double balance) {
        this.name = name;
        this.accNumber = accNumber;
        toWithdraw(balance);
    }

    public Bank(String name, int accNumber) {
        this.name = name;
        this.accNumber = accNumber;
    }

    public void setName(String name){
        this.name = name;
    }

    public String getName() {
        return name;
    }

    public void addBalance(double balance){
        this.balance += balance;
    }

    public void toWithdraw(double balance){
        this.balance -= balance - 5;
    }

    public double getBalance(){
        return balance;
    }
}
