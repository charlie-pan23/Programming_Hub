import java.util.Scanner;

public class SimpleSet {
    private static int[] elements;
    private int size;
    private int capacity = 0;

    public SimpleSet(int capa) {
        this.capacity = capa;
        this.elements = new int[capa];
        this.size = 0;
    } //defined a set that can add elements.

    public boolean add(int element) {
        for (int i = 0; i < size; i++) {
            if (elements[i] == element) {
                return false; // Element already exists in the set
            }
        }
        elements[size++] = element;
        return true;
    }

    public double getAverage() {
        if (size == 0) return 0;
        int sum = 0;
        for (int element : elements) {
            sum += element;
        }
        return (double) sum / size;
    }

    public int getMax() {
        if (size == 0) return Integer.MIN_VALUE;
        int max = elements[0];
        for (int i = 1; i < size; i++) {
            if (elements[i] > max) {
                max = elements[i];
            }
        }
        return max;
    }

    public int getMin() {
        if (size == 0) return Integer.MAX_VALUE;
        int min = elements[0];
        for (int i = 1; i < size; i++) {
            if (elements[i] < min) {
                min = elements[i];
            }
        }
        return min;
    }

    public static void displaySet(int size) {
        System.out.print("Set={");
        for (int i = 0; i < size + 1; i++) {
            System.out.print(elements[i] + (i < size ? ", " : ""));
        }
        System.out.println("}");
    }

    public static void DisplayAverage(int size) {
        System.out.println("[Item:Average]");
        double currentsum = 0;
        int maxavr = 0;
        for (int i = 1; i < size + 1; i++) {
            currentsum += elements[i - 1];
            currentsum /= i;
            if (currentsum > maxavr) {
                maxavr = (int) Math.floor(currentsum);
            }
        }
        for (int i = 1; i < size + 1; i++) {
            currentsum += elements[i - 1];
            currentsum /= i;
            System.out.printf("[\t%d:\t%-10.3f] ", i, currentsum);
            for (int j = 0; j < Math.floor(currentsum); j++) {
                System.out.print("+");
            }
            for (int j = 0; j < maxavr - Math.floor(currentsum) + 2; j++) {
                System.out.print(" ");
            }
            System.out.println("\t|");
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Choose the method:\t1\tor\t2:");
        int method = scanner.nextInt();
        System.out.print("Enter the number of elements in set: ");
        int numberOfElements = scanner.nextInt();
        SimpleSet set = new SimpleSet(numberOfElements);

        for (int i = 0; i < numberOfElements; i++) {
            System.out.print("Enter a new integer: ");
            double input = scanner.nextDouble();
            if (input == Math.round(input)) {
                int integerInput = (int) input;
                if (set.add(integerInput)) {
                    System.out.println("New element added: " + integerInput + ". There are " + set.size + " elements in the set now. ");
                    displaySet(i);
                    System.out.println(" ");
                } else {
                    System.out.println("The number is a duplicates");
                    i -= 1;
                }
            } else {
                System.out.println("The input value is NOT an integer!");
                i -= 1;
            }
        }

        if (method == 1) {
            System.out.println("The average of the set is: " + set.getAverage());
        } else if (method == 2) {
            System.out.println("Tendency of the average value");
            DisplayAverage(numberOfElements);
            double max = Double.parseDouble(String.valueOf(set.getMax()));
            double min = Double.parseDouble(String.valueOf(set.getMin()));
            double avr = set.getAverage();
            System.out.printf("max: %.3f, min: %.3f, average: %f\n", max, min, avr);
//            System.out.println(max+"\n"+min+"\n"+avr+"\n");
        }

    }
}