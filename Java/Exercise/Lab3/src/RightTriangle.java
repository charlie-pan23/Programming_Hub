import java.util.Scanner;

public class RightTriangle {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int a = scanner.nextInt();
        int b = scanner.nextInt();
        int c = scanner.nextInt();
        boolean check = false;
        if (a <= 0 || b <= 0 || c <= 0) { //positive?
            check = false;
        }else{

            int[] sides = {a, b, c};          //c longest
            int temp;
            for (int i = 0; i < 3; i++) {
                for (int j = i + 1; j < 3; j++) {
                    if (sides[i] > sides[j]) {
                        temp = sides[i];
                        sides[i] = sides[j];
                        sides[j] = temp;
                    }
                }
            }
            a = sides[0];
            b = sides[1];
            c = sides[2];

            check = (a * a + b * b == c * c);

        }


        if (check) {
            System.out.println("true");
        } else {
            System.out.println("false");
        }
        scanner.close();
    }


}