import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        while (t-- > 0) {
            int n = sc.nextInt();
            double p = sc.nextDouble();
            int i = sc.nextInt();
            if (p == 0) {
                System.out.println("0.0000");
            } else {
                double q = 1 - p;
                double qn = Math.pow(q, n);
                double qi = Math.pow(q, i - 1);
                double result = qi * p / (1 - qn);
                System.out.printf("%.4f%n", result);
            }
        }
        sc.close();
    }
}
