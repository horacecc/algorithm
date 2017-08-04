import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        boolean open = true;
        
        while (sc.hasNextLine()) {
            String line = sc.nextLine();
            StringBuilder sb = new StringBuilder();
            
            for (int i = 0; i < line.length(); i++) {
                char c = line.charAt(i);
                if (c == '"') {
                    sb.append(open ? "``" : "''");
                    open = !open;
                } else {
                    sb.append(c);
                }
            }
            System.out.println(sb);
        }
    }
}
