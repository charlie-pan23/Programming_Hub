public class MaxConsecutiveSum {
    public static int maxConsecutiveSum(int[] arr) {
        if (arr == null || arr.length == 0) {
            return 0;
        }

        int maxCurrent = arr[0];
        int maxGlobal = arr[0];

        for (int i = 1; i < arr.length; i++) {
            //update the current sum
            maxCurrent = Math.max(arr[i], maxCurrent + arr[i]);
            // update the global max sum
            maxGlobal = Math.max(maxGlobal, maxCurrent);
        }

        return maxGlobal;
    }

    public static void main(String[] args) {
        // test
        System.out.println(maxConsecutiveSum(new int[]{-3, 5, -2, 3, -1})); // 6
        System.out.println(maxConsecutiveSum(new int[]{1, -1})); // 1
    }
}