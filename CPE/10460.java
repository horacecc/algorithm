import java.math.BigInteger;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        BigInteger eleven = BigInteger.valueOf(11);
        
        while (sc.hasNextLine()) {
            String line = sc.nextLine().trim();
            if (line.equals("0")) break;
            
            BigInteger n = new BigInteger(line);
            if (n.mod(eleven).equals(BigInteger.ZERO)) {
                System.out.println(line + " is a multiple of 11");
            } else {
                System.out.println(line + " is not a multiple of 11");
            }
        }
        sc.close();
    }
}
