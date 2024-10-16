public class Dummy {

    private static int a = 3;
    private static int b = 4;
    private static int c = 5;

    public static void main(String... argumenets) {
        int a = 1, b = 2;
        System.out.println("" + a + (a - b) + c);
    }

//-------------------------------------------------------
//    public static int test(int a, int b, int c) {
//        b = c;
//        System.out.println(""+c+b+a);
//        return a + b + c;
//    }
//
//    public static void main(String[] argumenets) {
//        int a = 5, b = 4, c = 3;
//        a = test(c, b, a);
//        System.out.println("" + a + b + c);
//    }
//-------------------------------------------------------

//    public static void test(int two, int three) {
//        int one = two * three;
//        System.out.println("" + one + three + two);
//    }
//
//    public static void main(String... argumenets) {
//        int a = 7, b = 5, c = 3;
//        test(a, b);
//        System.out.println(a + b + c);
//    }
//-------------------------------------------------------

//    public static int foo(int input) {
//        int result;
//        result = input / 6 % 3;
//        return result;
//    }
//
//
//
//    public static void main(String... argumenets) {
//        int n;
//        n = foo(28);
//        System.out.println(n);
//    }
//-------------------------------------------------------

//    public static void foo(double c, int b, double a) {
//        b = (int) c;
//        System.out.println("" + a + " " + b + " " + c);
//    }
//
//    public static void main(String... argumenets) {
//        double a = 10.8, c = 5.6;
//        int b = 2;
//        foo(a, b, c);
//        b = (int) c;
//        System.out.println("" + a + " " + b + " " + c);
//    }

}

