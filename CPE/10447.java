import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        for (int i = 1; i <= n; i++) {
            long x1 = sc.nextLong();
            long y1 = sc.nextLong();
            long x2 = sc.nextLong();
            long y2 = sc.nextLong();
            long s1 = (x1 + y1) * (x1 + y1 + 1) / 2 + x1;
            long s2 = (x2 + y2) * (x2 + y2 + 1) / 2 + x2;
            System.out.println("Case " + i + ": " + (s2 - s1));
        }
        sc.close();
    }
}
