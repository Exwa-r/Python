import java.util.*;

public class Binary {
    public static void main(String[] args) {
        int i,j;
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter The Binary Number: ");
        String binary = sc.nextLine();
        String octal_num = " ";
        int index = binary.length()-1;
        sc.close();

        System.out.print("Binary to Octal Conversion ");
        for (i = binary.length()/2; i > 0; i--)
        {
            if (index == -1){
                break;
            }
            else{
                int power = 0,octal = 0;
                for ( j = 0 ; j<3 ; j++){
                    if (index == -1){
                        break;
                    }
                    else {
                        if (binary.charAt(index) == '1'){
                            octal += (Math.pow(2, power));
                        }
                        index--;
                        power++;
                    }
                }
                octal_num = Integer.toString(octal) + octal_num;
            }
            
        }
            System.out.println(octal_num);
    }
}