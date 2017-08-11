import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        while (sc.hasNextLine()) {
            String s = sc.nextLine();
            if (s.equals("0")) break;
            int sum = 0;
            for (int i = 0; i < s.length(); i++) {
                sum += s.charAt(i) - '0';
            }
            if (sum % 9 != 0) {
                System.out.println(s + " is not a multiple of 9.");
            } else {
                int degree = 1;
                while (sum > 9) {
                    int t = 0;
                    while (sum > 0) {
                        t += sum % 10;
                        sum /= 10;
                    }
                    sum = t;
                    degree++;
                }
                System.out.println(s + " is a multiple of 9 and has 9-degree " + degree + ".");
            }
        }
        sc.close();
    }
}
