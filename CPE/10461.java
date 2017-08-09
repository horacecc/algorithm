import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        while (sc.hasNextInt()) {
            int n = sc.nextInt();
            if (n == 0) break;
            String bin = Integer.toBinaryString(n);
            int cnt = 0;
            for (int i = 0; i < bin.length(); i++) {
                if (bin.charAt(i) == '1') cnt++;
            }
            System.out.println("The parity of " + bin + " is " + cnt + " (mod 2).");
        }
        sc.close();
    }
}
