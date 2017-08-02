import java.util.Scanner;

public class Main {
    static long[] units = {10000000, 100000, 1000, 100};
    static String[] names = {"kuti", "lakh", "hajar", "shata"};
    static StringBuilder sb;
    
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        for (int c = 1; sc.hasNext(); c++) {
            long n = sc.nextLong();
            sb = new StringBuilder();
            if (n == 0) sb.append(" 0");
            else convert(n);
            System.out.printf("%4d.%s%n", c, sb);
        }
    }
    
    static void convert(long n) {
        for (int i = 0; i < 4; i++) {
            if (n >= units[i]) {
                convert(n / units[i]);
                sb.append(" ").append(names[i]);
                n %= units[i];
            }
        }
        if (n > 0) sb.append(" ").append(n);
    }
}
