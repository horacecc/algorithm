import java.util.*;
public class Main {
    public static void main(String[] args) {
        int[] ary_c={120,210,170,200,1};
        double[] ary_f1={2.10,3.02,4.39,4.97,5.63};
        double[] ary_f2={2.10,2.68,3.61,4.01,4.50};
        Scanner scn = new Scanner(System.in);
        int n = scn.nextInt();
        double f1=0,f2=0;
        for(int i=0;n!=0;i++){
            if(i==ary_c.length)
                i--;
            if(n>ary_c[i]){
                n-=ary_c[i];
                f1+=ary_c[i]*ary_f1[i];
                f2+=ary_c[i]*ary_f2[i];
            }else{
                f1+=n*ary_f1[i];
                f2+=n*ary_f2[i];
                n=0;
            }
        }      
        System.out.println("Summer months:"+(Math.round(f1*100)+"").substring(0,(Math.round(f1*100)+"").length()-2)+"."+(Math.round(f1*100)+"").substring((Math.round(f1*100)+"").length()-2)+"\n"+"Non-Summer months:"+(Math.round(f2*100)+"").substring(0,(Math.round(f2*100)+"").length()-2)+"."+(Math.round(f2*100)+"").substring((Math.round(f2*100)+"").length()-2));
    }
}