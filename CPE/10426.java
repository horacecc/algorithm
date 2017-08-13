import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine().trim());
        br.readLine();
        
        StringBuilder sb = new StringBuilder();
        while (t-- > 0) {
            TreeMap<String, Integer> map = new TreeMap<>();
            int total = 0;
            String line;
            
            while ((line = br.readLine()) != null && !line.isEmpty()) {
                map.put(line, map.getOrDefault(line, 0) + 1);
                total++;
            }
            
            for (Map.Entry<String, Integer> e : map.entrySet()) {
                double percent = e.getValue() * 100.0 / total;
                sb.append(String.format("%s %.4f%n", e.getKey(), percent));
            }
            
            if (t > 0) sb.append("\n");
        }
        System.out.print(sb);
    }
}
