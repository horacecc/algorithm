import java.util.HashSet;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int caseNum = 1;
        while (sc.hasNext()) {
            int n = sc.nextInt();
            int[] b = new int[n];
            for (int i = 0; i < n; i++)
                b[i] = sc.nextInt();
            
            boolean isB2 = true;
            
            if (b[0] < 1)
                isB2 = false;
            
            for (int i = 1; i < n && isB2; i++) {
                if (b[i] <= b[i - 1])
                    isB2 = false;
            }
            
            HashSet<Integer> sums = new HashSet<>();
            for (int i = 0; i < n && isB2; i++) {
                for (int j = i; j < n && isB2; j++) {
                    int sum = b[i] + b[j];
                    if (sums.contains(sum))
                        isB2 = false;
                    else
                        sums.add(sum);
                }
            }
            
            System.out.println("Case #" + caseNum + ": " + 
                (isB2 ? "It is a B2-Sequence." : "It is not a B2-Sequence."));
            System.out.println();
            caseNum++;
        }
        sc.close();
    }
}
