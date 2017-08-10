import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        for (int i = 1; i <= n; i++) {
            long a = Long.parseLong(sc.next(), 2);
            long b = Long.parseLong(sc.next(), 2);
            System.out.print("Pair #" + i + ": ");
            if (gcd(a, b) > 1)
                System.out.println("All you need is love!");
            else
                System.out.println("Love is not all you need!");
        }
        sc.close();
    }

    static long gcd(long a, long b) {
        return b == 0 ? a : gcd(b, a % b);
    }
}
