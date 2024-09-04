import java.util.Scanner;

public class strongno {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        System.out.print("Enter a number: ");
        int num=sc.nextInt();
        int temp=num;
        int remainder;
        int sum=0;
        sc.close();

        while(temp>0){
            remainder=temp%10;
            int fact=1;
            for(int i=remainder;i>=1;i--){
                fact*=i;
            }
            temp=temp/10;
            sum+=fact;
        }
        if (num == sum)
        {
            System.out.println(num + " is a strong number.");
        }
        else
        {
            System.out.println(num + " is  a weak number.");
        }
    }
}