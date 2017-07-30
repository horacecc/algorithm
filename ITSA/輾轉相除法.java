import java.util.*;      
    
public class Main {      
    public static void main(String[] args){      
        Scanner cin = new Scanner(System.in);      
        int n1=cin.nextInt();  
        int n2=cin.nextInt();     
        int min=Math.min(n1,n2);  
        int max=Math.max(n1,n2);  
        for(int i=min;i>0;i--){  
            if(max%i==0 && min%i==0){  
                System.out.println(i);  
                break;  
            }  
        }  
    }       
}  