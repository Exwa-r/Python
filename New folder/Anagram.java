public class Anagram {
    public static void main(String[] args) {
        int i,j,count = 0,index = 0 , str1_length = 0;
        String str1 = "hellol";
        String str2 = "helllo";
        String Str1 = str1 + "/" ;
        while (Str1.charAt(index) != '/')
        {
            str1_length++;
            index++;
        }
        for (i = 0 ; i < str1_length ; i++)
        {
            for (j = 0 ; j < str2.length() ; j++) 
            {
                if (str1.charAt(i) == str2.charAt(j))
                {
                    count++;
                    break;
                }
            }
        }
        if (count == str1_length){
            System.out.println("The two strings are anagrams.");
        }
        else {
            System.out.println("The two strings are not anagrams.");
        }
    }
}
