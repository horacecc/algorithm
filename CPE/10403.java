import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        while (n-- > 0) {
            String s = sc.next();
            int dec = Integer.parseInt(s);
            int hex = Integer.parseInt(s, 16);
            System.out.println(Integer.bitCount(dec) + " " + Integer.bitCount(hex));
        }
        sc.close();
    }
}
