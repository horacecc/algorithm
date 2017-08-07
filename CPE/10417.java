import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        while (sc.hasNext()) {
            long s = sc.nextLong();
            long d = sc.nextLong();
            long sum = 0;
            while (sum < d) {
                sum += s;
                s++;
            }
            System.out.println(s - 1);
        }
        sc.close();
    }
}
