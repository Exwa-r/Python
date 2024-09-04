

// Input :alphabet
// Output :lph

// Input: alphabnjkmso
// Output:bjnkms


import java.util.Scanner;
public class Substring {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter a String : ");
        String str = scanner.nextLine();
        int  i , j ;
        String Temp_string = "";
        scanner.close();
        for (i = 0 ; i < str.length() ; i++) {
            String subString = "";
            if (str.charAt(i) == 'a' || str.charAt(i) == 'e' || str.charAt(i) == 'i' || str.charAt(i) == 'o' || str.charAt(i) == 'u'){
                for (j = i + 1 ; j < str.length() ; j++) {
                    if (str.charAt(j) == 'a' || str.charAt(j) == 'e' || str.charAt(j) == 'i' || str.charAt(j) == 'o' || str.charAt(j) == 'u'){
                        break;
                    }
                    else{
                        subString += str.charAt(j);
                    }
                }
                if (subString.length() > Temp_string.length()){
                    Temp_string = subString;
                }
            }
        }
        System.out.println(Temp_string);
    }
}