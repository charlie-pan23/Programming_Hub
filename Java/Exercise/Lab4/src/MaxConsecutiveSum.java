public class MaxConsecutiveSum {
    public static int maxConsecutiveSum(int[] arr) {
        if (arr == null || arr.length == 0) {
            return 0;
        }

        int maxCurrent = arr[0];
        int maxGlobal = arr[0];

        for (int i = 1; i < arr.length; i++) {
            // 更新当前元素的连续和
            maxCurrent = Math.max(arr[i], maxCurrent + arr[i]);
            // 更新全局最大和
            maxGlobal = Math.max(maxGlobal, maxCurrent);
        }

        return maxGlobal;
    }

    public static void main(String[] args) {
        // 测试用例
        System.out.println(maxConsecutiveSum(new int[]{-3, 5, -2, 3, -1})); // 输出应该是6
        System.out.println(maxConsecutiveSum(new int[]{1, -1})); // 输出应该是1
    }
}