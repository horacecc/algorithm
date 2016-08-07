import java.util.*;
import java.lang.*;
import java.io.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int ans,num,A = 0,B = 0;
        boolean end = false;
        ans = sc.nextInt();
        int ansarr[] = new int[4];
        ansarr[0] = ans /1000;
        ansarr[1] = (ans % 1000)/100;
        ansarr[2] = ((ans % 1000)%100)/10;
        ansarr[3] = ((ans % 1000)%100)%10;
        int numarr[] = new int[4];
        while(end == false){
            num = sc.nextInt();
            if(num !=0000){
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
                System.out.println(A + "A" + B + "B");
                A=0;
                B=0; 
            }else
                end = true;
        }
    }
}
