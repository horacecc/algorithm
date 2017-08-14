import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int field = 0;
        
        while (sc.hasNextInt()) {
            int n = sc.nextInt();
            int m = sc.nextInt();
            
            if (n == 0 && m == 0) break;
            
            if (field > 0) System.out.println();
            field++;
            
            char[][] grid = new char[n][m];
            for (int i = 0; i < n; i++) {
                grid[i] = sc.next().toCharArray();
            }
            
            int[][] result = new int[n][m];
            int[] dx = {-1, -1, -1, 0, 0, 1, 1, 1};
            int[] dy = {-1, 0, 1, -1, 1, -1, 0, 1};
            
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < m; j++) {
                    if (grid[i][j] == '*') {
                        result[i][j] = -1;
                    } else {
                        int count = 0;
                        for (int k = 0; k < 8; k++) {
                            int ni = i + dx[k];
                            int nj = j + dy[k];
                            if (ni >= 0 && ni < n && nj >= 0 && nj < m && grid[ni][nj] == '*') {
                                count++;
                            }
                        }
                        result[i][j] = count;
                    }
                }
            }
            
            System.out.println("Field #" + field + ":");
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < m; j++) {
                    if (result[i][j] == -1) {
                        System.out.print('*');
                    } else {
                        System.out.print(result[i][j]);
                    }
                }
                System.out.println();
            }
        }
        sc.close();
    }
}
