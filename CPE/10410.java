import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        boolean first = true;
        
        while (sc.hasNextLine()) {
            String line = sc.nextLine();
            
            if (!first) {
                System.out.println();
            }
            first = false;
            
            int[] freq = new int[128];
            for (int i = 0; i < line.length(); i++) {
                char c = line.charAt(i);
                if (c >= 32 && c < 127) {
                    freq[c]++;
                }
            }
            
            List<int[]> list = new ArrayList<>();
            for (int i = 32; i < 127; i++) {
                if (freq[i] > 0) {
                    list.add(new int[]{i, freq[i]});
                }
            }
            
            Collections.sort(list, (a, b) -> {
                if (a[1] != b[1]) return a[1] - b[1];
                return b[0] - a[0];
            });
            
            for (int[] p : list) {
                System.out.println(p[0] + " " + p[1]);
            }
        }
    }
}
