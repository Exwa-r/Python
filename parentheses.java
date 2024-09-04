// check valid parenthesis

// Input :(())
// Output:True

// Input:(({])
// Output:False

import java.util.*;
public class parentheses {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String parenthesis = scanner.nextLine();
        int i , j , open_paranthesis = 0 , close_paranthesis = 0;
        scanner.close();
        for (i = 0 ; i < parenthesis.length() ; i++) {
            if (parenthesis.charAt(i) == '(' || parenthesis.charAt(i) == '{' || parenthesis.charAt(i) == '[') {
                open_paranthesis ++ ;
            }
        }
        for (j = 0 ; j < parenthesis.length() ; j++) {
            if (parenthesis.charAt(j) == ')' || parenthesis.charAt(j) == '}' || parenthesis.charAt(j) == ']') {
                close_paranthesis ++ ;
            }
        }
        if (open_paranthesis == close_paranthesis) { 
            System.out.println("True");
        }
        else {
            System.out.println("False");
        }
    }
}