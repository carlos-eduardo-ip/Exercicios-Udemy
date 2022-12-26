package application;

public class Product {

    private String name;
    private double price;
    private int quantity;

    public String toString(){
        return name
                + ", $ "
                + String.format("%.2f", price)
                +", "
                +quantity
                + " units, Total: $ "
                + String.format("%.2f", totalValueInStock());
    }

    public double totalValueInStock(){
        return this.quantity * this.price;
    }

    public void setName(String name){
        this.name = name;
    }

    public void setPrice(double price){
        this.price = price;
    }

    public void addProducts(int quantity){
        this.quantity +=  quantity;
    }

    public void removeProducts(int quantity){
        this.quantity -= quantity;
    }
}
