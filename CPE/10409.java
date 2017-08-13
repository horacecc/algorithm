import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        while (sc.hasNextInt()) {
            int n = sc.nextInt();
            int[] a = new int[n];
            for (int i = 0; i < n; i++) {
                a[i] = sc.nextInt();
            }
            Arrays.sort(a);
            int mid1 = a[(n - 1) / 2];
            int mid2 = a[n / 2];
            int count = 0;
            for (int i = 0; i < n; i++) {
                if (a[i] >= mid1 && a[i] <= mid2) {
                    count++;
                }
            }
            System.out.println(mid1 + " " + count + " " + (mid2 - mid1 + 1));
        }
    }
}
