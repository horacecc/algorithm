import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        final double R = 6440.0;
        
        while (sc.hasNext()) {
            double s = sc.nextDouble();
            double angle = sc.nextDouble();
            String unit = sc.next();
            
            if (unit.equals("min")) {
                angle /= 60.0;
            }
            
            angle = angle % 360.0;
            if (angle > 180.0) {
                angle = 360.0 - angle;
            }
            
            double r = R + s;
            double rad = Math.toRadians(angle);
            
            double arc = r * rad;
            double chord = 2.0 * r * Math.sin(rad / 2.0);
            
            System.out.printf("%.6f %.6f%n", arc, chord);
        }
        sc.close();
    }
}
