import java.util.*;     
public class Main {     
    public static void main(String[] args) {  
        Scanner sc=new Scanner(System.in);  
        int num=sc.nextInt();
        for(int i=0;i<num;i++){
            int n1=sc.nextInt(),count=0;
            for(int j=2;j<n1;j++)
                if(n1%j==0)
                    count++;
            System.out.println(count/2);
        }
    }  
}  