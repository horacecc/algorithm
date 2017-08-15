import java.util.Scanner;

public class Main {
    static int maxX, maxY;
    static boolean[][] scent = new boolean[51][51];
    static int[] dx = {0, 1, 0, -1};
    static int[] dy = {1, 0, -1, 0};
    
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        maxX = sc.nextInt();
        maxY = sc.nextInt();
        
        while (sc.hasNext()) {
            int x = sc.nextInt();
            int y = sc.nextInt();
            char dir = sc.next().charAt(0);
            String cmds = sc.next();
            
            int d = dirToInt(dir);
            boolean lost = false;
            
            for (int i = 0; i < cmds.length() && !lost; i++) {
                char c = cmds.charAt(i);
                if (c == 'L') {
                    d = (d + 3) % 4;
                } else if (c == 'R') {
                    d = (d + 1) % 4;
                } else if (c == 'F') {
                    int nx = x + dx[d];
                    int ny = y + dy[d];
                    if (nx < 0 || nx > maxX || ny < 0 || ny > maxY) {
                        if (!scent[x][y]) {
                            scent[x][y] = true;
                            lost = true;
                        }
                    } else {
                        x = nx;
                        y = ny;
                    }
                }
            }
            
            System.out.println(x + " " + y + " " + intToDir(d) + (lost ? " LOST" : ""));
        }
    }
    
    static int dirToInt(char c) {
        switch (c) {
            case 'N': return 0;
            case 'E': return 1;
            case 'S': return 2;
            case 'W': return 3;
        }
        return 0;
    }
    
    static char intToDir(int d) {
        return "NESW".charAt(d);
    }
}
