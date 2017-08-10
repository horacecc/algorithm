import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        while (t-- > 0) {
            int n = sc.nextInt();
            int p = sc.nextInt();
            int[] h = new int[p];
            for (int i = 0; i < p; i++) {
                h[i] = sc.nextInt();
            }
            boolean[] hartal = new boolean[n + 1];
            for (int i = 0; i < p; i++) {
                for (int j = h[i]; j <= n; j += h[i]) {
                    hartal[j] = true;
                }
            }
            int count = 0;
            for (int day = 1; day <= n; day++) {
                int mod = day % 7;
                if (mod != 6 && mod != 0 && hartal[day]) {
                    count++;
                }
            }
            System.out.println(count);
        }
        sc.close();
    }
}
