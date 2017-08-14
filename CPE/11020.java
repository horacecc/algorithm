import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[][] f = new int[128][10];
        f['c'] = new int[]{0,1,1,1,0,0,1,1,1,1};
        f['d'] = new int[]{0,1,1,1,0,0,1,1,1,0};
        f['e'] = new int[]{0,1,1,1,0,0,1,1,0,0};
        f['f'] = new int[]{0,1,1,1,0,0,1,0,0,0};
        f['g'] = new int[]{0,1,1,1,0,0,0,0,0,0};
        f['a'] = new int[]{0,1,1,0,0,0,0,0,0,0};
        f['b'] = new int[]{0,1,0,0,0,0,0,0,0,0};
        f['C'] = new int[]{0,0,1,0,0,0,0,0,0,0};
        f['D'] = new int[]{1,1,1,1,0,0,1,1,1,0};
        f['E'] = new int[]{1,1,1,1,0,0,1,1,0,0};
        f['F'] = new int[]{1,1,1,1,0,0,1,0,0,0};
        f['G'] = new int[]{1,1,1,1,0,0,0,0,0,0};
        f['A'] = new int[]{1,1,1,0,0,0,0,0,0,0};
        f['B'] = new int[]{1,1,0,0,0,0,0,0,0,0};
        
        int t = Integer.parseInt(sc.nextLine());
        while (t-- > 0) {
            String s = sc.nextLine();
            int[] cnt = new int[10];
            int[] prev = new int[10];
            for (int i = 0; i < s.length(); i++) {
                char c = s.charAt(i);
                int[] cur = f[c];
                for (int j = 0; j < 10; j++) {
                    if (cur[j] == 1 && prev[j] == 0) {
                        cnt[j]++;
                    }
                    prev[j] = cur[j];
                }
            }
            StringBuilder sb = new StringBuilder();
            for (int i = 0; i < 10; i++) {
                if (i > 0) sb.append(" ");
                sb.append(cnt[i]);
            }
            System.out.println(sb);
        }
    }
}
