import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        while (sc.hasNextLine()) {
            String line = sc.nextLine();
            int maxDigit = -1, sum = 0;
            for (int i = 0; i < line.length(); i++) {
                char c = line.charAt(i);
                int val = -1;
                if (c >= '0' && c <= '9') val = c - '0';
                else if (c >= 'A' && c <= 'Z') val = c - 'A' + 10;
                else if (c >= 'a' && c <= 'z') val = c - 'a' + 36;
                if (val >= 0) {
                    sum += val;
                    if (val > maxDigit) maxDigit = val;
                }
            }
            if (maxDigit < 0) {
                System.out.println("such number is impossible!");
                continue;
            }
            int minBase = maxDigit + 1;
            if (minBase < 2) minBase = 2;
            boolean found = false;
            for (int base = minBase; base <= 62; base++) {
                if (sum % (base - 1) == 0) {
                    System.out.println(base);
                    found = true;
                    break;
                }
            }
            if (!found) System.out.println("such number is impossible!");
        }
    }
}
