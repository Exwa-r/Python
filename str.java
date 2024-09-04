// Find if a String2 is substring of String1. If it is, return the index of the first occurrence. else return -1.
// Eg 1:Input:
//         String 1: test123string
//          String 2: 123
//         Output: 4
// Eg 2: Input:
//         String 1: testing12
//         String 2: 1234 
//         Output: -1




import java.util.Scanner;
public class str {
    public static void main(String[] args) {
        Scanner sc=new Scanner (System.in);
        System.out.println("Enter the first string :");
        String str1=sc.nextLine();
        System.out.println("Enter the second string :");
        String str2=sc.nextLine();
        int store=0;
        int count=0,c=0;
        sc.close();

        for(int i=0;i<str1.length();i++){
            if(count==1){
                 store=i-1;
            }
            for(int j=0;j<str2.length();j++){
                if(str1.charAt(i)==str2.charAt(j)){
                    
                    count++;
                    
                    
                    break;
                }
                else if(count>=1){
                    c++;

                }
            }
        }
         if(c==0 && count==str2.length()){
                System.out.println(store);
            }
            else{
                System.err.println(-1);
            }
    }
}