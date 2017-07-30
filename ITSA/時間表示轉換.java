import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner scn = new Scanner(System.in);
        int n=scn.nextInt();
        while(n--!=0){
            int num=scn.nextInt(),a=0,b=0,c=0;
            System.out.print(num+"=");
            a=num/86400;
            num%=86400;
            b=num/3600;
            num%=3600;
            c=num/60;
            num%=60;
            System.out.printf("%02d,%02d,%02d,%02d\n",a,b,c,num);
        }
    }
}
