import java.util.Arrays;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        
        while (t-- > 0) {
            int r = sc.nextInt();
            int[] s = new int[r];
            
            for (int i = 0; i < r; i++) {
                s[i] = sc.nextInt();
            }
            
            Arrays.sort(s);
            int median = s[r / 2];
            
            int dist = 0;
            for (int i = 0; i < r; i++) {
                dist += Math.abs(s[i] - median);
            }
            
            System.out.println(dist);
        }
        sc.close();
    }
}
