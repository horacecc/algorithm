import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        while (n-- > 0) {
            long s = sc.nextLong();
            long d = sc.nextLong();
            if ((s + d) % 2 != 0 || s < d) {
                System.out.println("impossible");
            } else {
                long a = (s + d) / 2;
                long b = (s - d) / 2;
                System.out.println(a + " " + b);
            }
        }
        sc.close();
    }
}
