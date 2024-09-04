import java.util.Scanner;

public class fibonacci {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int num1 = 0;
        int num2 = 1;
        int sum = 0;
        System.out.print("Enter the range :");
        int range = sc.nextInt();
        System.out.print(num1 + " " + num2 + " ");
        sc.close();
        
        for (int i = num1; i < range; i++) {
            sum = num1 + num2;
            num1 = num2;
            num2 = sum;
            if (sum <= range){
                System.out.print(sum + " ");
            }
            else{
                break;
            }       
        }
    }
}