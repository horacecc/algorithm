import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        while (sc.hasNextInt()) {
            int n = sc.nextInt();
            int max = 0;
            for (int borrow = 0; borrow <= 2; borrow++) {
                int total = n;
                int empty = n + borrow;
                while (empty >= 3) {
                    int newBottles = empty / 3;
                    total += newBottles;
                    empty = empty % 3 + newBottles;
                }
                if (empty >= borrow) {
                    max = Math.max(max, total);
                }
            }
            System.out.println(max);
        }
        sc.close();
    }
}
