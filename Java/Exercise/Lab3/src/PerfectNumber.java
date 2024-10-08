import java.util.Scanner;
public class PerfectNumber {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        int n = Integer.parseInt(sc.nextLine());
        int sum = 1;
        if (n <= 1){
            System.out.println("false");
        }else{

            for (int i = 2; i <= Math.round(Math.sqrt(n)); i++) {
                if (n % i == 0) {
                    sum += i;
                    sum += n / i;
                }
            }
            if(sum == n){
                System.out.println("true");
            } else if (sum != n) {
                System.out.println("false");
            }


        }


    }

}
