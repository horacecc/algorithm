import java.util.Scanner;

public class Main {
    static char[][] grid;
    static int M, N;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();
        while (T-- > 0) {
            M = sc.nextInt();
            N = sc.nextInt();
            int Q = sc.nextInt();
            grid = new char[M][N];
            for (int i = 0; i < M; i++) {
                grid[i] = sc.next().toCharArray();
            }
            System.out.println(M + " " + N + " " + Q);
            while (Q-- > 0) {
                int r = sc.nextInt();
                int c = sc.nextInt();
                System.out.println(solve(r, c));
            }
        }
        sc.close();
    }

    static int solve(int r, int c) {
        char ch = grid[r][c];
        int size = 1;
        while (true) {
            int top = r - size;
            int bot = r + size;
            int left = c - size;
            int right = c + size;
            if (top < 0 || bot >= M || left < 0 || right >= N) break;
            if (!check(ch, top, bot, left, right)) break;
            size++;
        }
        return 2 * size - 1;
    }

    static boolean check(char ch, int top, int bot, int left, int right) {
        for (int i = top; i <= bot; i++) {
            if (grid[i][left] != ch || grid[i][right] != ch) return false;
        }
        for (int j = left + 1; j < right; j++) {
            if (grid[top][j] != ch || grid[bot][j] != ch) return false;
        }
        return true;
    }
}
