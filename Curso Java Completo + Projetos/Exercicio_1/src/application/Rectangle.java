package application;

public class Rectangle {
    private double width;
    private double height;

    public String toString(){
        return "AREA = "
                + String.format("%.2f",area())
                + "\nPERIMETER = "
                + String.format("%.2f",perimentro())
                + "\nDIAGONAL = "
                + String.format("%.2f",diagonal());
    }

    private double area(){
        return width * height;
    }
    private double perimentro(){
        return 2 * (width + height);
    }

    private double diagonal(){
        return Math.sqrt(width * width + height * height);
    }

    public void setWidth(double width) {
        this.width = width;
    }

    public void setHeight(double height) {
        this.height = height;
    }
}
