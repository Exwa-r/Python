import java.util.ArrayList;
import java.util.Scanner;

public class assanddess {
    public static void main(String[] args) {
        //Sort first half in ascending order and second half in descending. 
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
        int mid = n / 2;

        for (int i = 0; i < mid; i++) {
            for (int j = i + 1; j < mid; j++) {
                if (arr.get(i) > arr.get(j)) {
                    int temp = arr.get(i);
                    arr.set(i, arr.get(j));
                    arr.set(j, temp);
                }
            }
        }
        System.out.println(arr);
        
        for (int i = mid; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                if (arr.get(i) < arr.get(j)) {
                    int temp = arr.get(i);
                    arr.set(i, arr.get(j));
                    arr.set(j, temp);
                }
            }
        }
        
        System.out.println("Sorted array:");
        System.out.println(arr);
    }
}
