import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        while (sc.hasNextLine()) {
            String a = sc.nextLine();
            String b = sc.nextLine();
            
            int[] countA = new int[26];
            int[] countB = new int[26];
            
            for (char c : a.toCharArray()) {
                countA[c - 'a']++;
            }
            
            for (char c : b.toCharArray()) {
                countB[c - 'a']++;
            }
            
            StringBuilder result = new StringBuilder();
            for (int i = 0; i < 26; i++) {
                int common = Math.min(countA[i], countB[i]);
                for (int j = 0; j < common; j++) {
                    result.append((char) ('a' + i));
                }
            }
            
            System.out.println(result);
        }
        
        sc.close();
    }
}
