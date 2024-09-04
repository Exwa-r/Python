import java.util.Scanner;

public class Duplicate {
    public static void main(String[] args) {
        
        Scanner sc=new Scanner(System.in);
        System.out.print("Enter the String :");
        String a=sc.nextLine();
     
        sc.close();
        for(int i=0;i<a.length();i++){
            int count=0;
            for(int j=i+1;j<a.length();j++){
                if(a.charAt(i)==a.charAt(j)){
                    count++;
                }
            }
            if(count==0){
                System.out.print(a.charAt(i));
            }
        }
    }
}
