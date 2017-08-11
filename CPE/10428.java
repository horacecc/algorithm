import java.util.Scanner;

public class Main {
    static boolean[] sieve = new boolean[1000001];
    
    public static void main(String[] args) {
        generateSieve();
        Scanner sc = new Scanner(System.in);
        while (sc.hasNextInt()) {
            int n = sc.nextInt();
            if (sieve[n]) {
                int rev = reverse(n);
                if (rev != n && sieve[rev]) {
                    System.out.println(n + " is emirp.");
                } else {
                    System.out.println(n + " is prime.");
                }
            } else {
                System.out.println(n + " is not prime.");
            }
        }
        sc.close();
    }
    
    static void generateSieve() {
        for (int i = 2; i <= 1000000; i++) sieve[i] = true;
        for (int i = 2; i * i <= 1000000; i++) {
            if (sieve[i]) {
                for (int j = i * i; j <= 1000000; j += i) {
                    sieve[j] = false;
                }
            }
        }
    }
    
    static int reverse(int n) {
        int rev = 0;
        while (n > 0) {
            rev = rev * 10 + n % 10;
            n /= 10;
        }
        return rev;
    }
}
