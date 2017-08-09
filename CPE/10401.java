import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        long[] fib = new long[45];
        fib[0] = 1;
        fib[1] = 2;
        for (int i = 2; i < 45; i++) {
            fib[i] = fib[i - 1] + fib[i - 2];
        }
        
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        
        while (n-- > 0) {
            long num = sc.nextLong();
            long original = num;
            
            int maxIdx = 0;
            for (int i = 44; i >= 0; i--) {
                if (fib[i] <= num) {
                    maxIdx = i;
                    break;
                }
            }
            
            StringBuilder sb = new StringBuilder();
            for (int i = maxIdx; i >= 0; i--) {
                if (fib[i] <= num) {
                    sb.append('1');
                    num -= fib[i];
                } else {
                    sb.append('0');
                }
            }
            
            System.out.println(original + " = " + sb.toString() + " (fib)");
        }
        sc.close();
    }
}
