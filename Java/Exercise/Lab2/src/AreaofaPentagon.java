import java.util.Scanner;
public class AreaofaPentagon {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        String input = sc.nextLine();
        double r = Double.parseDouble(input);
        double s = 2 * r * Math.sin((Math.PI/5));
        double area = (5 * Math.pow(s, 2)) / (4 * Math.tan(Math.PI / 5));

        System.out.println("Area = " + area);



    }
}
