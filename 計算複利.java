import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner scn = new Scanner(System.in);
        double r = scn.nextFloat()+1;
        int n = scn.nextInt();
        int p = scn.nextInt();
        double ans= 0;
        for(int i=0;i<n;i++)
            ans=(ans+p)*r;
        System.out.println((int)ans);
    }
}