import java.util.Scanner;
import java.math.BigInteger;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        while (sc.hasNextLine()) {
            String line = sc.nextLine();
            String[] nums = line.trim().split("\\s+");
            BigInteger ans = new BigInteger(nums[0]);
            for (int i = 1; i < nums.length; i++) {
                if (!nums[i].isEmpty()) {
                    ans = ans.multiply(new BigInteger(nums[i]));
                }
            }
            System.out.println(ans);
        }
        sc.close();
    }
}
