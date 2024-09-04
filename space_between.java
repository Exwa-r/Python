// input
// this is programming
// output
// thisispro gramming

// kuduthuruka sentance la space count pani total characters la divide pani 17/2 =8 8 
// charaters pirichu remaining characters first la irunthu add panitu varanum



public class space_between {
    public static void main(String[] args) {
        String str = "this is programming rhdtrf ghgf";
        String Temp_string = str + '/';
        String sub_Sring = "";
        int index = 0  , count = 0 ;
        int length = str.length();
        while (Temp_string.charAt(index) != '/'){
            if (Temp_string.charAt(index) == ' '){
                count++;
                index++;
            }
            else{
                sub_Sring += Temp_string.charAt(index);
                index++;
            }
        }
        System.out.println(sub_Sring + " " + count + " " + length);
        int divide = length / count;
        System.out.println(divide);
        String final_string = "";
        int indx = 0;
        for(int i = 0 ; i < count ; i++) {
            for (int j = 1 ; j <= divide ; j++) {
                if (indx < sub_Sring.length()){
                    final_string += sub_Sring.charAt(indx);
                    indx++;
                }
            }
            final_string += " ";
        }
        System.out.println(final_string);
    }
}