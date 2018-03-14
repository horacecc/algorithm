import java.util.*;
import java.lang.*;
import java.io.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int numss=sc.nextInt();
        for(int iii=0;iii<numss;iii++){
        int ans,num,A = 0,B = 0;

        ans = sc.nextInt();
        int ansarr[] = new int[4];
        ansarr[0] = ans /1000;
        ansarr[1] = (ans % 1000)/100;
        ansarr[2] = ((ans % 1000)%100)/10;
        ansarr[3] = ((ans % 1000)%100)%10;
        int numarr[] = new int[4];

            num = sc.nextInt();

                for(int j = 0;j < numarr.length;j++){
                    numarr[0] = num /1000;
                    numarr[1] = (num % 1000)/100;
                    numarr[2] = ((num % 1000)%100)/10;
                    numarr[3] = ((num % 1000)%100)%10;
                }
                for(int x = 0;x < ansarr.length;x++)
                    for(int y = 0;y < numarr.length;y++)
                        if(x==y){
                            if(ansarr[x] == numarr[y])
                                A++;
                        }else
                            if(ansarr[x] == numarr[y])
                                B++;
                System.out.println(A + "a" + B + "b");
                A=0;
                B=0; 



    }}
}
