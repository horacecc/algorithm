import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n;
        while ((n = sc.nextInt()) != 0) {
            int top = 1, north = 2, west = 3;
            int bottom = 7 - top, south = 7 - north, east = 7 - west;
            for (int i = 0; i < n; i++) {
                String cmd = sc.next();
                int tmp;
                if (cmd.equals("north")) {
                    tmp = top;
                    top = south;
                    south = bottom;
                    bottom = north;
                    north = tmp;
                } else if (cmd.equals("south")) {
                    tmp = top;
                    top = north;
                    north = bottom;
                    bottom = south;
                    south = tmp;
                } else if (cmd.equals("east")) {
                    tmp = top;
                    top = west;
                    west = bottom;
                    bottom = east;
                    east = tmp;
                } else if (cmd.equals("west")) {
                    tmp = top;
                    top = east;
                    east = bottom;
                    bottom = west;
                    west = tmp;
                }
            }
            System.out.println(top);
        }
    }
}
