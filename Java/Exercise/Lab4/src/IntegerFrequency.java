public class IntegerFrequency {
    public static int getFrequency(int[] input, int num) {
        int frequency = 0;
        for(int s : input){
            if(s == num){
                frequency++;
            }
        }
        return frequency;
    }

    public static void main(String[] args) {
        int[] arr1 = {1, 2, 1};
        int num1 = 1;
        int num2 = 2;
        System.out.println(getFrequency(arr1, num1));
        System.out.println(getFrequency(arr1, num2));
    }

}
