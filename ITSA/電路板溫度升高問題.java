import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int m = sc.nextInt();
        sc.nextLine();
        
        while (m-- > 0) {
            String line = sc.nextLine();
            String[] parts = line.split(",");
            double Ti = Double.parseDouble(parts[0]);
            int i = Integer.parseInt(parts[1]);
            
            System.out.printf("%.4f%n", Ti + 2.71828 * (1 + i) * i / 2);
        }
        
        sc.close();
    }
}
