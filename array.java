// Input: 1,2,3,4,5,6,7,8,9
// Output: 9,2,7,4,5,6,3,8,1


import java.util.ArrayList;
import java.util.Scanner;

public class array {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Enter numbers, with 0 to end");
        ArrayList<Integer> arr = new ArrayList<Integer>();
        while (true) {
            int input = scanner.nextInt();
            if (input == 0) {
                break;
            }
            arr.add(input);
        }
        System.out.println("You entered: " + arr);
        scanner.close();

        int n = arr.size();

        for (int i = 0; i < n; i+=2) {
            for (int j = i + 2; j < n; j+=2) {
                if (arr.get(i) < arr.get(j)) {
                    int temp = arr.get(i);
                    arr.set(i, arr.get(j));
                    arr.set(j, temp);
                }
            }
        }
        for (int i = 1; i < n; i+=2) {
            for (int j = i + 2; j < n; j+=2) {
                if (arr.get(i) > arr.get(j)) {
                    int temp = arr.get(i);
                    arr.set(i, arr.get(j));
                    arr.set(j, temp);
                }
            }
        }
        System.out.println();
        System.out.println("Sorted array:");
        System.out.println(arr);
    }
    }

