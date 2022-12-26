package application;

public class Employee{
    private String name;
    private double grossSalary;
    private double tax;


    public String toString() {
        return name
                + ", $ "
                + String.format("%.2f", netSalary());
    }

    public double netSalary() {
        return grossSalary - tax;
    }

    public void increaseSalary(double percentage) {
        this.grossSalary += (grossSalary / 100) * percentage;
    }

    public void setName(String name) {
        this.name = name;
    }

    public void setTax(double tax) {
        this.tax = tax;
    }

    public void setGrossSalary(double grossSalary) {
        this.grossSalary = grossSalary;
    }

}
