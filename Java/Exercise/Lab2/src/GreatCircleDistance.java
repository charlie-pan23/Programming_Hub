import java.util.Scanner;

public class GreatCircleDistance {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String input = sc.nextLine();
        double x1 = Double.parseDouble(input);
        input = sc.nextLine();
        double y1 = Double.parseDouble(input);
        input = sc.nextLine();
        double x2 = Double.parseDouble(input);
        input = sc.nextLine();
        double y2 = Double.parseDouble(input);

        double r = 6371.0;

        double halfX = (x2 - x1) / 2.0;
        double halfY = (y2 - y1) / 2.0;

        double sinHalfX = Math.sin(Math.toRadians(halfX));
        double cosX1 = Math.cos(Math.toRadians(x1));
        double cosX2 = Math.cos(Math.toRadians(x2));
        double sinHalfY = Math.sin(Math.toRadians(halfY));

        double term1 = Math.pow(sinHalfX, 2);
        double term2 = cosX1 * cosX2 * Math.pow(sinHalfY, 2);

        double inner = Math.sqrt(term1 + term2);
        double dist = 2 * r * Math.asin(inner);

        System.out.println(dist+" kilometres");
    }
}
