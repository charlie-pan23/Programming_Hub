import java.util.Scanner;

public class PandemicSpread {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int init = Integer.parseInt(sc.nextLine());
        int numInfect = Integer.parseInt(sc.nextLine());
        int population = Integer.parseInt(sc.nextLine());

        int days = 1;
        int infected = init;

        while (infected < population) {
            infected += infected * numInfect;
            days++;
        }
        System.out.println(days);

    }
}
