import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = Integer.parseInt(sc.nextLine());
        int[] freq = new int[26];
        
        for (int i = 0; i < n; i++) {
            String line = sc.nextLine().toUpperCase();
            for (char c : line.toCharArray()) {
                if (c >= 'A' && c <= 'Z') {
                    freq[c - 'A']++;
                }
            }
        }
        
        List<int[]> list = new ArrayList<>();
        for (int i = 0; i < 26; i++) {
            if (freq[i] > 0) {
                list.add(new int[]{i, freq[i]});
            }
        }
        
        Collections.sort(list, (a, b) -> {
            if (b[1] != a[1]) return b[1] - a[1];
            return a[0] - b[0];
        });
        
        for (int[] p : list) {
            System.out.println((char)('A' + p[0]) + " " + p[1]);
        }
    }
}
