import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner scn = new Scanner(System.in);
        int[] n = new int[]{scn.nextInt(),scn.nextInt(),scn.nextInt(),scn.nextInt()};
        Arrays.sort(n);
        if(n[1]==n[2]&&n[1]==n[3]&&n[1]==n[0]&&n[2]==n[3]&&n[2]==n[0]&&n[3]==n[0])
            System.out.println("WIN");
        else if(n[1]!=n[2]&&n[1]!=n[3]&&n[1]!=n[0]&&n[2]!=n[3]&&n[2]!=n[0]&&n[3]!=n[0])
            System.out.println("R");
        else if(n[0]!=n[1]&&n[1]==n[2]&&n[2]==n[3]||n[3]!=n[2]&&n[0]==n[1]&&n[1]==n[2])
            System.out.println("R");
        else
            System.out.println(n[3]+n[2]);
    }
}