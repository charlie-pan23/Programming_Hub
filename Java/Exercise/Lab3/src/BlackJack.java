//import java.util.Scanner;
//
//public class BlackJack {
//    public static void main(String[] args) {
//        Scanner sc = new Scanner(System.in);
//        int a = Integer.parseInt(sc.nextLine());
//        int b = Integer.parseInt(sc.nextLine());
//        if (a > 21 && b > 21){
//            System.out.println(-1);
//        }
//        else {
//            int diffa = Math.abs(a - 21);
//            int diffb = Math.abs(b - 21);
//
//            // 比较差值，输出最接近21的值
//            if (a <= 21 && (b > 21 || diffa < diffb)) {       //diffa <= diffb
//                System.out.println(a);
//            } else if (b <= 21 && (a > 21 || diffb < diffa)) {
//                System.out.println(b);
//            } else {
//                System.out.println(-1);
//            }
//
//        }
//
//    }
//}

import java.util.Scanner;
public class BlackJack{
public static void main(String[] args){
    Scanner sc = new Scanner(System.in);
    int a = Integer.parseInt(sc.nextLine());
    int b = Integer.parseInt(sc.nextLine());
    if (a > 21 && b > 21){
        System.out.println(-1);
    }
    else {
        if(a <= 21 && b > 21){
            System.out.println(a);
        }else if (a > 21 && b <= 21){
            System.out.println(b);
        }else{
            int diffa = Math.abs(a - 21);
            int diffb = Math.abs(b - 21);

            if (diffa <= diffb) {
                System.out.println(a);
            } else if ( diffb < diffa) {
                System.out.println(b);
            } else {
                System.out.println(-1);
            }
        }
    }

}
}

