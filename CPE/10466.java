import java.util.Scanner;
import java.util.ArrayList;

public class Main {
    static int[] cost = new int[36];

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();
        for (int t = 1; t <= T; t++) {
            for (int i = 0; i < 36; i++) {
                cost[i] = sc.nextInt();
            }
            int Q = sc.nextInt();
            if (t > 1) System.out.println();
            System.out.println("Case " + t + ":");
            for (int q = 0; q < Q; q++) {
                int n = sc.nextInt();
                solve(n);
            }
        }
        sc.close();
    }

    static void solve(int n) {
        int minCost = Integer.MAX_VALUE;
        ArrayList<Integer> bases = new ArrayList<>();
        for (int base = 2; base <= 36; base++) {
            int c = getCost(n, base);
            if (c < minCost) {
                minCost = c;
                bases.clear();
                bases.add(base);
            } else if (c == minCost) {
                bases.add(base);
            }
        }
        System.out.print("Cheapest base(s) for number " + n + ":");
        for (int b : bases) {
            System.out.print(" " + b);
        }
        System.out.println();
    }

    static int getCost(int n, int base) {
        if (n == 0) return cost[0];
        int total = 0;
        while (n > 0) {
            total += cost[n % base];
            n /= base;
        }
        return total;
    }
}
