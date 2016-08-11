import java.util.*;      
    
public class Main      
{      
    public static void main(String[] args)      
    {      
        Scanner cin = new Scanner(System.in);      
    
        while(cin.hasNext()) {    
            int a,val1=cin.nextInt();     
            val1 = (int)Math.abs(val1);     
            for(a=2;a<=val1; a++)      
                if(val1%a == 0)        
                    break;    
            if(a != val1)      
                System.out.println("NO");      
            else      
                System.out.println("YES");      
        }    
    }       
}  