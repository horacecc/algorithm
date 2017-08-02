import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = Integer.parseInt(sc.nextLine());
        
        TreeMap<String, Integer> map = new TreeMap<>();
        
        for (int i = 0; i < n; i++) {
            String line = sc.nextLine();
            String country = line.split(" ")[0];
            map.put(country, map.getOrDefault(country, 0) + 1);
        }
        
        for (Map.Entry<String, Integer> entry : map.entrySet()) {
            System.out.println(entry.getKey() + " " + entry.getValue());
        }
    }
}
