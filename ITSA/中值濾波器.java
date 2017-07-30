import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        while (n-- > 0) {
            int m = sc.nextInt();
            int[] seq = new int[3];
            seq[0] = sc.nextInt();
            seq[1] = sc.nextInt();
            System.out.print(seq[0] + " ");
            m -= 2;
            while (m-- > 0) {
                seq[2] = sc.nextInt();
                if (seq[2] <= seq[0]) {
                    if (seq[0] <= seq[1])
                        seq[1] = seq[0];
                    else if (seq[1] <= seq[2])
                        seq[1] = seq[2];
                } else {
                    if (seq[1] < seq[0])
                        seq[1] = seq[0];
                    else if (seq[2] < seq[1])
                        seq[1] = seq[2];
                }
                System.out.print((seq[0] = seq[1]) + " ");
                seq[1] = seq[2];
            }
            System.out.println(seq[2]);
        }
        sc.close();
    }
}
