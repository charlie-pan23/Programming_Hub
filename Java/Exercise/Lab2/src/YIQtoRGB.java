import java.util.Scanner;
public class YIQtoRGB {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        double Y = sc.nextDouble();
        double I = sc.nextDouble();
        double Q = sc.nextDouble();

        int r = (int) Math.round((Y + 0.956 * I + 0.619 * Q) * 255);
        int g = (int) Math.round((Y - 0.272 * I - 0.647 * Q) * 255);
        int b = (int) Math.round((Y - 1.106 * I + 1.703 * Q) * 255);

        r = Math.min(255, Math.max(0, r));
        g = Math.min(255, Math.max(0, g));
        b = Math.min(255, Math.max(0, b));

        System.out.printf("red = %d\ngreen = %d\nblue = %d%n", r, g, b);

    }
}
