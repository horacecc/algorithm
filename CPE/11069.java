import java.util.*;

public class Main {
    static int M;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        StringBuilder sb = new StringBuilder();

        while (sc.hasNextInt()) {
            int N = sc.nextInt();
            M = sc.nextInt();
            sb.append(N).append(" ").append(M).append("\n");

            if (N == 0 && M == 0) break;

            Integer[] arr = new Integer[N];
            for (int i = 0; i < N; i++) {
                arr[i] = sc.nextInt();
            }

            Arrays.sort(arr, (a, b) -> {
                int modA = a % M;
                int modB = b % M;

                if (modA != modB) return modA - modB;

                boolean oddA = Math.abs(a) % 2 == 1;
                boolean oddB = Math.abs(b) % 2 == 1;

                if (oddA && !oddB) return -1;
                if (!oddA && oddB) return 1;

                if (oddA) return b - a;
                return a - b;
            });

            for (int i = 0; i < N; i++) {
                sb.append(arr[i]).append("\n");
            }
        }

        System.out.print(sb);
    }
}
