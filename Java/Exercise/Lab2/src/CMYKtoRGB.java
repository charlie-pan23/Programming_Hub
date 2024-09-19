import java.util.Scanner;
public class CMYKtoRGB {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String input = sc.nextLine();
        double cyan = Double.parseDouble(input);
        input = sc.nextLine();
        double magenta = Double.parseDouble(input);
        input = sc.nextLine();
        double yellow = Double.parseDouble(input);
        input = sc.nextLine();
        double black = Double.parseDouble(input);

        double white = (1.0-black);
        int red = (int) Math.round(255*white*(1-cyan));
        int green = (int) Math.round(255*white*(1-magenta));
        int blue = (int) Math.round(255*white*(1-yellow));

        System.out.println("red = " + red + "\ngreen = " + green + "\nblue = " + blue);


    }
}
