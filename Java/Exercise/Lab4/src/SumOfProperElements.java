public class SumOfProperElements {
    public static int sumOfProperElements(int[] nums) {
        int sum = 0;

        if (nums == null || nums.length == 0) {
            return sum;
        }

        for (int i = 0; i < nums.length; i++) {
            if (nums[i] % (i + 1) == 0) {
                sum += nums[i];
            }
        }
        return sum;

    }

    public static void main(String[] args) {
        // test
        System.out.println(sumOfProperElements(new int[]{1, 2, 6})); // 9
        System.out.println(sumOfProperElements(new int[]{10, 25})); // 10
    }

}
