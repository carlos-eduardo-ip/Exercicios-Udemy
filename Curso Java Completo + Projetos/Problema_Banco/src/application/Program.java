package application;

import entities.Bank;

import java.util.Scanner;

public class Program {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Bank user;

        System.out.println("Hello, welcome to IP Bank!\n");
        System.out.print("Enter Account number: ");
        int accNumber = sc.nextInt();
        System.out.print("Enter account holder: ");
        sc.next();
        String name = sc.nextLine();
        System.out.print("Is there na initial deposit (y/n)?");
        char request = sc.next().charAt(0);

        if (request == 'y') {
            System.out.print("Enter initial deposit value: ");
            double iniDeposit = sc.nextDouble();
            user = new Bank(name, accNumber, iniDeposit);
        } else {
            user = new Bank(name, accNumber);
        }

        System.out.println("Account data: " + user);

        int option;
        do {
            Menu.menu();
            System.out.print("Select the option: ");
            option = sc.nextInt();

            switch (option) {

                case 1:
                    System.out.print("Enter a deposit value: ");
                    user.addBalance(sc.nextDouble());
                    System.out.println("Update account data: "+ user);
                    break;
                case 2:
                    System.out.print("Enter a withdraw value: ");
                    user.toWithdraw(sc.nextDouble());
                    System.out.println("Update account data: "+ user);
                    break;
                case 3:
                    System.out.println("Balance: $ " + String.format("%.2f", user.getBalance()));
                    break;
                case 4:
                    System.out.print("Do you want to update your name (y/n)?");
                    char upName = sc.next().charAt(0);

                    if (upName == 'y') {
                        System.out.print("Write your new name: ");
                        sc.nextLine();
                        user.setName(sc.nextLine());
                        System.out.println("Your name has been updated: "+ user.getName());
                        System.out.println("\nLet's go back to the menu!\n");
                    } else {
                        System.out.println("\nLet's go back to the menu!\n");
                    }
                    break;
                case 5:
                    System.out.println("\nCheck back often!\n");
                    break;
            }
        } while (option != 5);
        sc.close();
    }
}
