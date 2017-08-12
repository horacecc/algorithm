import java.util.*;    
public class Main{    
    public static void main(String[] args){    
        Scanner cin = new Scanner(System.in);
        int m=cin.nextInt();
        for(int i=0;i<m;i++){
            int count=cin.nextInt();
            int n1=cin.nextInt();
            int d1=cin.nextInt();
            int n2=cin.nextInt();
            int d2=cin.nextInt();
            int total=2147483647;
            int n1_ans=0;
            int n2_ans=0;
            for(int j=0;j<=(count/n1);j++){
                for(int k=0;k<=(count/n2);k++){
                    if((j*n1+k*n2)==count)
                        if((j*d1+k*d2)<total){
                            total=(j*d1+k*d2);
                            n1_ans=j;
                            n2_ans=k;
                        }                    
                }
            }
            if(total==2147483647)
                System.out.println("false");
            else
                System.out.println(n1_ans+" "+n2_ans);
        }       
    }     
}  