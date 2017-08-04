import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        while (sc.hasNextInt()) {
            int n = sc.nextInt();
            int[] arr = new int[n];
            
            for (int i = 0; i < n; i++) {
                arr[i] = sc.nextInt();
            }
            
            if (n == 1) {
                System.out.println("Jolly");
                continue;
            }
            
            boolean[] seen = new boolean[n];
            boolean jolly = true;
            
            for (int i = 1; i < n; i++) {
                int diff = Math.abs(arr[i] - arr[i - 1]);
                if (diff < 1 || diff >= n || seen[diff]) {
                    jolly = false;
                    break;
                }
                seen[diff] = true;
            }
            
            System.out.println(jolly ? "Jolly" : "Not jolly");
        }
        
        sc.close();
    }
}
