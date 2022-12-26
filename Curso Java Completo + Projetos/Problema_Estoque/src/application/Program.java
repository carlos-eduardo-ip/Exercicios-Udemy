package application;

import java.util.Scanner;

public class Program {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        Product client = new Product();

        System.out.println("Enter Product data: ");
        System.out.print("Name: ");
        client.setName(sc.nextLine());
        System.out.print("Price: ");
        client.setPrice(sc.nextDouble());
        System.out.print("Quantity in stock: ");
        client.addProducts(sc.nextInt());

        System.out.println("\nProduct data: " + client);

        System.out.print("\nEnter the number of products to be add in stock: ");
        client.addProducts(sc.nextInt());
        System.out.println("Update date: " + client);

        System.out.print("\nEnter the number of products to be removed in stock: ");
        client.removeProducts(sc.nextInt());
        System.out.println("Update date: " + client);
        sc.close();
    }
}
