import java.util.Scanner;
import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        while (sc.hasNextLong()) {
            long n = sc.nextLong();
            long m = sc.nextLong();
            
            if (n <= 1 || m <= 1) {
                System.out.println("Boring!");
                continue;
            }
            
            ArrayList<Long> seq = new ArrayList<>();
            seq.add(n);
            boolean valid = true;
            
            while (n > 1) {
                if (n % m != 0) {
                    valid = false;
                    break;
                }
                n /= m;
                seq.add(n);
            }
            
            if (valid) {
                StringBuilder sb = new StringBuilder();
                for (int i = 0; i < seq.size(); i++) {
                    if (i > 0) sb.append(" ");
                    sb.append(seq.get(i));
                }
                System.out.println(sb.toString());
            } else {
                System.out.println("Boring!");
            }
        }
    }
}
