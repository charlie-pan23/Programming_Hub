import java.util.Scanner;

public class HailstoneSequenceLength {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        System.out.println(fLen(n));
        scanner.close();
    }

    public static int fLen(int n) {
        if (n == 1) {
            return 1; // 序列的最后一个数字是1
        } else {
            return 1 + fLen(n % 2 == 0 ? n / 2 : 3 * n + 1); // 递归调用
        }
    }
}


//import java.util.Scanner;
//
//public class HailstoneSequenceLength {
//    public static void main(String[] args) {
//        Scanner scanner = new Scanner(System.in);
//        int n = scanner.nextInt();
//
//        int length = 1; // 初始数字n本身是序列的第一个数字
//        while (n != 1) {
//            if (n % 2 == 0) {
//                n = n / 2;
//            } else {
//                n = 3 * n + 1;
//            }
//            length++;
//        }
//
//        System.out.println(length);
//        scanner.close();
//    }
//
//}