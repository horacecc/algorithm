import java.util.ArrayList;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        ArrayList<String> lines = new ArrayList<>();
        int maxLen = 0;
        
        while (sc.hasNextLine()) {
            String line = sc.nextLine();
            lines.add(line);
            maxLen = Math.max(maxLen, line.length());
        }
        
        int n = lines.size();
        
        for (int i = 0; i < n; i++) {
            StringBuilder sb = new StringBuilder(lines.get(i));
            while (sb.length() < maxLen) {
                sb.append(' ');
            }
            lines.set(i, sb.toString());
        }
        
        for (int col = 0; col < maxLen; col++) {
            StringBuilder sb = new StringBuilder();
            for (int row = n - 1; row >= 0; row--) {
                sb.append(lines.get(row).charAt(col));
            }
            String result = sb.toString().replaceAll("\\s+$", "");
            System.out.println(result);
        }
        
        sc.close();
    }
}
