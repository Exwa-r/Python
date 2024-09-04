public class swap {
    public static void main(String[] args) {
        // swap two number without temporary variables
        int a = 5, b = 10;
        a = a + b;
        b = a - b;
        a = a - b;
        System.out.println("After swapping: a = " + a + ", b = " + b);
        // swap two number using XOR operator
        a = a ^ b;
        b = a ^ b;
        a = a ^ b;
        System.out.println("After swapping using XOR: a = " + a + ", b = " + b);
    }
}
