import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[] days = {0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
        String[] weekday = {"Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"};
        
        int t = sc.nextInt();
        while (t-- > 0) {
            int m = sc.nextInt();
            int d = sc.nextInt();
            
            int total = 0;
            for (int i = 1; i < m; i++) {
                total += days[i];
            }
            total += d - 1;
            
            System.out.println(weekday[total % 7]);
        }
        sc.close();
    }
}
