// array number frequency count eg:input {1,2,3,2,3}
// 2 
// output
// 2 times

import java.util.Scanner;

public class frequency_count {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int arr[] = {1,2,3,2,3};
        System.out.print("Enter a Frequency in the List : ");
        int frequency = scanner.nextInt();
        int count = 0;
        scanner.close();
        for (int i = 0 ; i < arr.length ; i++){
            if (frequency == arr[i]){
                count++;
            }
        }
        System.out.println(count + " times");      
    }
}
