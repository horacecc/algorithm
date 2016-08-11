import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner scn = new Scanner(System.in);
        int n = scn.nextInt();
        for(int i=0;i<n;i++){
            int[] ary_n = {scn.nextInt(),scn.nextInt(),scn.nextInt()};
            Arrays.sort(ary_n);
            if(ary_n[0]>59&&ary_n[1]>59&&ary_n[2]>59||(ary_n[2]+ary_n[1]+ary_n[0])>=220){
                System.out.println("P");
            }else if(ary_n[0]<60&&ary_n[1]>59&&ary_n[2]>59||ary_n[2]>79){
                System.out.println("M");
            }else{
                System.out.println("F");
            }
        }
    }
}