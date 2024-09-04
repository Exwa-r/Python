// 1.  input
// this is programming
// output
// thisispro gramming


public class Str1 {
    public static void main(String[] args) {
         String b="this is programming rhdtrf ghgf";
          int count=0;
         

       int n=b.length();
       b+="/";
       int i=0;
         String c="";
         
      
       while(b.charAt(i)!='/') {
        if(b.charAt(i)==' '){
            count++;
           
        }
     i++;}
       

        int tot=n/count;
        
       
      String a="";

        for( i=0;i<n;i++){
            if(i<=tot+1 && b.charAt(i)!=' '){
                c+=b.charAt(i);
               
            }
            if(i>tot+1){
              
                a+=b.charAt(i);
            }

            
        }
        System.out.println(c+" "+a);
    }
}