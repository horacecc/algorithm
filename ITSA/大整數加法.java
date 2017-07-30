import java.math.BigInteger;  
import java.util.*;  
    
public class Main {  
    
    public static void main(String[] args) {  
        Scanner sc=new Scanner(System.in);  
           int n=sc.nextInt();  
           BigInteger arr,tot;  
           for(int i=0;i<n;i++){  
               arr=sc.nextBigInteger();  
               tot=sc.nextBigInteger();  
               System.out.println(tot.add(arr));   
           }  
    }  
}  