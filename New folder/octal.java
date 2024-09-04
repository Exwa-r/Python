import java.util.*;

public class octal {
    public static void main(String[] args) {
      int i,decimal = 0,power = 0,remainder = 0;
      Scanner sc = new Scanner(System.in);
      System.out.print("Enter The Octal Number: ");
      String octal_nu = " ";
      String octal = sc.nextLine();
      System.out.print("Octal to Decimal Conversion ");
      sc.close();
      for (i = octal.length()-1; i >= 0; i--){
        int octal_num = octal.charAt(i)-'0';
        decimal +=(octal_num*(Math.pow(8, power)));
        power++;  
      }
      System.out.println(decimal);

      System.out.print("Decimal to Octal Conversion ");
      for ( i = 0 ; i < octal.length() ; i++){
        remainder = decimal%8;
        decimal = decimal/8;
        octal_nu = String.valueOf(remainder)+octal_nu;
      }
      System.out.println(octal_nu);
      
    }
  }

