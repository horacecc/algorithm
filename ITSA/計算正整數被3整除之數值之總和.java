import java.util.*;      
    
public class Main      
{      
    public static void main(String[] args)      
    {      
        Scanner cin = new Scanner(System.in);      
    
        while(cin.hasNext()) {    
            int ans=0,n1=cin.nextInt();     
            for(int a=3;a<=n1;a=a+3){  
                ans+=a;  
            }  
            System.out.println(ans);  
        }    
    }       
} 