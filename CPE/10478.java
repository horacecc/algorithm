import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        for (int c = 1; c <= t; c++) {
            sc.next();
            sc.next();
            int n = sc.nextInt();
            long[][] m = new long[n][n];
            boolean sym = true;
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    m[i][j] = sc.nextLong();
                    if (m[i][j] < 0) sym = false;
                }
            }
            if (sym) {
                for (int i = 0; i < n && sym; i++) {
                    for (int j = 0; j < n && sym; j++) {
                        if (m[i][j] != m[n - 1 - i][n - 1 - j]) sym = false;
                    }
                }
            }
            System.out.println("Test #" + c + ": " + (sym ? "Symmetric." : "Non-symmetric."));
        }
        sc.close();
    }
}
