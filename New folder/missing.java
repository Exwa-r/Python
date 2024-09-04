// public class missing {
//     public static void main(String[] args) {
//         // finding missing numbers using bitwise operators
//         int[] arr = {1, 2, 3, 5, 6, 8, 9, 10};
//         int n = arr.length;
//         int missing = (n * (n + 1)) / 2;
//         for (int i = 0; i < n; i++) {
//             missing ^= arr[i];
//         }
//         System.out.println("Missing number: " + missing);
//     }
// }


// import java.util.Scanner;

// public class missing {

//      void numMissing(int small,int large,int[] arr){
 
    

//         for(int k=small;k<large;k++){
//             int count=0;
//             for(int y=0;y<arr.length;y++){
//             if(k==arr[y]){
//                 count++;
//                 break;

//             }
            
//         }
//         if(count==0){
//             System.out.println(k);
//         }
// }
// }




// void mulMissing(int small,int large,int arr_length,int[ ] arr){       
   


// int w=1,mul=1,h=0;


 

//        while (mul!=large) {
//         h=0;
       
//         mul=small;
//         mul*=w;
//         for(int q=0;q<arr_length;q++){
//         if(mul==arr[q])
//         {
//             h++;
//         }
        
        
       

//     }
//      if(h==0){
//             System.out.println(mul);

//         }
//     w++;
// }
// }

  

//     public static void main(String[] args) {
//                 Scanner sc=new Scanner (System.in); 
//                 missing mi=new missing();   
//         int large,small,n;
     
      
//         System.out.print("Enter the total number of array :");
//         n=sc.nextInt();
//         int[] arr=new int[n];
//            int arr_length=arr.length;
//         System.out.println("Enter the numbers :");
//         for(int i=0;i<n;i++){
//             arr[i]=sc.nextInt();
//         }
//         sc.close();
//         large=arr[0];
//          small=arr[0];

//         for (int j=0 ;j<arr.length;j++){
//             if(large<arr[j]){
//                 large=arr[j];
//             }
           

//             if(small>arr[j]){
//                 small=arr[j];
//             }


//         }

    
//     int f=0; 
   
//     for(int b:arr){
//         if(small==0 || b<=0){
//             break;
//         }
//         if(b%small==0){
//                 f++;
//             }
//             }
       
// System.out.println("Missing numbers :");
// if(f<arr_length){
      
            
//             mi.numMissing(small, large, arr);
        
//     }
// if(f==arr_length){
         
            
//             mi.mulMissing(small, large, arr_length, arr);
        
//     }
//      }
//     }


public class missing {

    public static void main(String[] args) {
        // finding missing number in a array
        int[] arr = {1, 2, 3, 5, 6, 8, 9, 10};
        int n = arr.length;
        int missing = (n * (n + 1)) / 2;
        for (int i = 0; i < n; i++) {
            missing ^= arr[i];
        }
        System.out.println("Missing number: " + missing);
    }
}