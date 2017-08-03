import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        String keyboard = "`1234567890-=qwertyuiop[]\\asdfghjkl;'zxcvbnm,./";
        Scanner sc = new Scanner(System.in);
        
        while (sc.hasNextLine()) {
            String line = sc.nextLine().toLowerCase();
            StringBuilder result = new StringBuilder();
            
            for (int i = 0; i < line.length(); i++) {
                char c = line.charAt(i);
                int idx = keyboard.indexOf(c);
                
                if (idx >= 2) {
                    result.append(keyboard.charAt(idx - 2));
                } else {
                    result.append(c);
                }
            }
            System.out.println(result);
        }
        sc.close();
    }
}
