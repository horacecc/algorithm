import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        while (sc.hasNextLong()) {
            long n = sc.nextLong();
            if (n == 0) break;
            System.out.println(digitalRoot(n));
        }
        sc.close();
    }

    static long digitalRoot(long n) {
        while (n >= 10) {
            long sum = 0;
            while (n > 0) {
                sum += n % 10;
                n /= 10;
            }
            n = sum;
        }
        return n;
    }
}
