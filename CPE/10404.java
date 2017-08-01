import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        while (sc.hasNextLong()) {
            long a = sc.nextLong();
            long b = sc.nextLong();
            
            if (a == 0 && b == 0) break;
            
            int carry = 0, count = 0;
            
            while (a > 0 || b > 0) {
                int sum = (int)(a % 10) + (int)(b % 10) + carry;
                carry = sum / 10;
                if (carry > 0) count++;
                a /= 10;
                b /= 10;
            }
            
            if (count == 0) {
                System.out.println("No carry operation.");
            } else if (count == 1) {
                System.out.println("1 carry operation.");
            } else {
                System.out.println(count + " carry operations.");
            }
        }
        
        sc.close();
    }
}
