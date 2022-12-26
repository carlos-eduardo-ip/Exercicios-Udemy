package application;

import java.util.Scanner;

public class Program {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Employee user = new Employee();

        System.out.print("Nome: ");
        user.setName(sc.nextLine());

        System.out.print("Gross salary: ");
        user.setGrossSalary(sc.nextDouble());

        System.out.print("Tax: ");
        user.setTax(sc.nextDouble());
        System.out.println("Employee: "+ user);

        System.out.print("Which percentage to increase salary? ");
        user.increaseSalary(sc.nextDouble());
        System.out.println("Updated data: "+ user);
        sc.close();
    }
}
