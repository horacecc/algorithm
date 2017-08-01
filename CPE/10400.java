import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        while (sc.hasNextInt()) {
            int i = sc.nextInt();
            int j = sc.nextInt();
            int lo = Math.min(i, j);
            int hi = Math.max(i, j);
            int maxLen = 0;
            
            for (int n = lo; n <= hi; n++) {
                maxLen = Math.max(maxLen, cycleLength(n));
            }
            
            System.out.println(i + " " + j + " " + maxLen);
        }
        sc.close();
    }
    
    static int cycleLength(long n) {
        int len = 1;
        while (n != 1) {
            if (n % 2 == 1) {
                n = 3 * n + 1;
            } else {
                n = n / 2;
            }
            len++;
        }
        return len;
    }
}
