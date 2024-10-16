public class MaxProduct {

    public static int maxProduct(int[] arr) {
        if (arr == null || arr.length < 2) {
            return 0;
        }

        int max1 = Integer.MIN_VALUE;
        int max2 = Integer.MIN_VALUE;
        int min1 = Integer.MAX_VALUE;
        int min2 = Integer.MAX_VALUE;

        for (int num : arr) {
            if (num > max1) {
                max2 = max1;
                max1 = num;
            } else if (num > max2) {
                max2 = num;
            }

            if (num < min1) {
                min2 = min1;
                min1 = num;
            } else if (num < min2) {
                min2 = num;
            }
        }

        return Math.max(max1 * max2, min1 * min2);
    }

    public static void main(String[] args) {
        // Test cases
        System.out.println(maxProduct(new int[]{-10, 5, -2, 1, 6})); // should return 30
        System.out.println(maxProduct(new int[]{-1, 2})); // should return -2
        System.out.println(maxProduct(new int[]{1})); // should return 0

        // Additional test cases
        System.out.println(maxProduct(new int[]{-1, -2, -3, -4})); // should return 12
        System.out.println(maxProduct(new int[]{0, 1, 2, 3, 4})); // should return 12
        System.out.println(maxProduct(new int[]{-1, 1})); // should return 1
        System.out.println(maxProduct(new int[]{-1, -2, 3, 4})); // should return 12
    }
}