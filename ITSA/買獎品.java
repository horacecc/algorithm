import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner scn = new Scanner(System.in);
        int n = scn.nextInt();
        while (n-- != 0) {
            int b = scn.nextInt(), t = scn.nextInt(), s = scn.nextInt(), arr[] = new int[s], tot = 0;
            for (int i = 0; i < s; i++)
                arr[i] = scn.nextInt();
            Arrays.sort(arr);
            for (int i = 0; i < t; i++)
                tot += arr[i];
            if (b - tot >= 0)
                System.out.println(tot);
            else
                System.out.println("Impossible");
        }
    }
}