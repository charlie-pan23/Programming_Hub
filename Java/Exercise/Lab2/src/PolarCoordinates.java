import java.util.Scanner;

public class PolarCoordinates {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String input = sc.nextLine();
        double x = Double.parseDouble(input);
        input = sc.nextLine();
        double y = Double.parseDouble(input);

        double r =Math.sqrt(Math.pow(x,2)+Math.pow(y,2));
        double theta = Math.atan2(y,x);

        System.out.println("r = "+r+"\ntheta = "+theta);
    }

}
