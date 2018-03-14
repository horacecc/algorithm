import java.util.*;
import java.lang.*;
import java.io.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int nums=sc.nextInt();
        forI:
        for(int i=0;i<nums;i++){
            int x=sc.nextInt();
            int n=sc.nextInt();
            int[][] arys=new int[n][2];
            for(int j=0;j<n;j++){
                arys[j][0]=sc.nextInt();
                arys[j][1]=sc.nextInt();
            }
            forJ:
            for(int j=1;j<=x;j++){
                int sum=0;
                while(true){
                    sum+=j;
                    for(int k=0;k<n;k++){
                        if(sum<arys[k][1]&&sum>arys[k][0]){
                            if(j!=x)
                                continue forJ;
                            else{
                                System.out.println(j);
                                continue forI;
                            }                               
                        }
                    }
                    if(sum>=x){
                        System.out.println(j);
                        continue forI;
                    }
                }    
                
            }
        }
    }
}
