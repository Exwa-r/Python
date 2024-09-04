// import java.util.Scanner;

public class alpha {
    public static void main(String[] args) {
        // Scanner sc = new Scanner(System.in);
        int i,j,k,n;
        String alpha = "a5d3vc12";

        for ( i = 0; i < alpha.length(); i++) {
            String number = "";
            if (Character.isLetter(alpha.charAt(i))) {
                for ( j = i+1; j < alpha.length() ; j++) {
                    if (Character.isDigit(alpha.charAt(j))){
                        number += alpha.charAt(j);
                        continue;
                    }
                    else{
                        break;
                    }
                }
                if (number == ""){
                    System.out.println("Enter a Valid String");
                    break;
                }
                else{
                    n = Integer.parseInt(number);
                for(k = 0;k < n; k++) {
                    System.out.println(alpha.charAt(i));
                }
                }
                
            } 
            else{
                continue;
            }
            
        }
    }        
}

