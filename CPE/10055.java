import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        while (sc.hasNextLong()) {
            long a = sc.nextLong();
            long b = sc.nextLong();
            
            long diff = a - b;
            if (diff < 0) diff = -diff;
            
            System.out.println(diff);
        }
            sc.close();
    }
}
