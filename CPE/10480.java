import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        while (sc.hasNextInt()) {
            int a = sc.nextInt();
            int b = sc.nextInt();
            if (a == 0 && b == 0) break;
            int lo = (int) Math.ceil(Math.sqrt(a));
            int hi = (int) Math.floor(Math.sqrt(b));
            int count = Math.max(0, hi - lo + 1);
            System.out.println(count);
        }
        sc.close();
    }
}
