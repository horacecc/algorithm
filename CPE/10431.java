import java.util.Scanner;
import java.math.BigInteger;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        while (sc.hasNextLine()) {
            long x = Long.parseLong(sc.nextLine().trim());
            String[] parts = sc.nextLine().trim().split("\\s+");
            int n = parts.length - 1;
            if (n == 0) {
                System.out.println(0);
                continue;
            }
            BigInteger result = BigInteger.valueOf(n).multiply(new BigInteger(parts[0]));
            for (int i = 1; i < n; i++) {
                result = result.multiply(BigInteger.valueOf(x)).add(
                    BigInteger.valueOf(n - i).multiply(new BigInteger(parts[i]))
                );
            }
            System.out.println(result);
        }
    }
}
