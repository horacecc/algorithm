import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        while (sc.hasNext()) {
            double x1 = sc.nextDouble(), y1 = sc.nextDouble();
            double x2 = sc.nextDouble(), y2 = sc.nextDouble();
            double x3 = sc.nextDouble(), y3 = sc.nextDouble();
            double x4 = sc.nextDouble(), y4 = sc.nextDouble();
            
            double rx, ry;
            if (eq(x1, x3) && eq(y1, y3)) {
                rx = x2 + x4 - x1;
                ry = y2 + y4 - y1;
            } else if (eq(x1, x4) && eq(y1, y4)) {
                rx = x2 + x3 - x1;
                ry = y2 + y3 - y1;
            } else if (eq(x2, x3) && eq(y2, y3)) {
                rx = x1 + x4 - x2;
                ry = y1 + y4 - y2;
            } else {
                rx = x1 + x3 - x2;
                ry = y1 + y3 - y2;
            }
            System.out.printf("%.3f %.3f%n", rx, ry);
        }
    }
    
    static boolean eq(double a, double b) {
        return Math.abs(a - b) < 1e-9;
    }
}
