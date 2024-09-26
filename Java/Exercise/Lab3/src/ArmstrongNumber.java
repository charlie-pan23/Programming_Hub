import java.util.Scanner;

public class ArmstrongNumber {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int a = scanner.nextInt();
        int k = scanner.nextInt();
        scanner.close();
        int count = 0;
        int number = a;
        int originalNumber, remainder, result = 0, n = 0;
        while (count < k) {

            result = 0;
            n = 0;
            originalNumber = number;
            while (originalNumber != 0) {
                remainder = originalNumber % 10;//按位取出
                originalNumber /= 10;           //右移一位
                n++;                            //数位数
            }

            originalNumber = number;
            while (originalNumber != 0) {
                remainder = originalNumber % 10;
                result += Math.pow(remainder, n);
                originalNumber /= 10;
            }

            if (result == number) {
                System.out.println(number);
                count++;
            }
            number++;
        }
    }
}
