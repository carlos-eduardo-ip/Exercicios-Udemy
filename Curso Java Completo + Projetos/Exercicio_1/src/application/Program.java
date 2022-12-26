package application;

import java.util.Scanner;

public class Program {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Rectangle user = new Rectangle();

        System.out.println("Enter rectangle width and height: ");
        user.setWidth(sc.nextDouble());
        user.setHeight(sc.nextDouble());
        System.out.println(user);
        sc.close();

    }
}
