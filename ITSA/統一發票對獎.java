import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner scn = new Scanner(System.in);
        String s1 = scn.next(), s2 = scn.next(), s3 = scn.next(), s4 = scn.next();
        int ans[] = new int[7], n = scn.nextInt(), tot = 0, m[] = { 200000, 40000, 10000, 4000, 1000, 200 };
        while (n-- != 0) {
            String str = scn.next();
            if (s1.equals(str)) {
                ans[0]++;
                tot += 2000000;
                continue;
            }
            for (int i = 0; i <= 5; i++) {
                if (str.indexOf(s2.substring(i), i) >= 0) {
                    ans[i + 1]++;
                    tot += m[i];
                    break;
                } else if (str.indexOf(s3.substring(i), i) >= 0) {
                    ans[i + 1]++;
                    tot += m[i];
                    break;
                } else if (str.indexOf(s4.substring(i), i) >= 0) {
                    ans[i + 1]++;
                    tot += m[i];
                    break;
                }
            }
        }
        for (int i = 0; i < ans.length; i++) {
            if (i != 0)
                System.out.print(" ");
            System.out.print(ans[i]);
        }
        System.out.printf("\n%d\n", tot);
    }
}