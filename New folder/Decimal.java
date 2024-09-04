import java.util.*;

public class Decimal {
    public static void main(String[] args) {
      int i,decimal = 0,power = 0,remainder = 0;
      Scanner sc = new Scanner(System.in);
      System.out.print("Enter The Binary Number: ");
      String binary_num = "";
      String binary = sc.nextLine();
      sc.close();

      System.out.print("Binary to Decimal Conversion ");
      for (i = binary.length()-1; i >= 0; i--){
        if (binary.charAt(i) == '1'){
          decimal += (Math.pow(2, power));
        }
        power++;  
      }
      System.out.println(decimal);
      
      System.out.print("Decimal to Binary Conversion ");
      for ( i = 0 ; i < binary.length() ; i++){
        remainder = decimal%2;
        decimal = decimal/2;
        binary_num = String.valueOf(remainder)+binary_num;
      }
      System.out.println(binary_num);
    }
  }