import java.util.*;  
import java.text.DecimalFormat;  
public class Main {  
    public static void main(String[] args) {  
        Scanner sc=new Scanner(System.in);  
        float max=Float.MIN_VALUE,n,min=Float.MAX_VALUE;    
        DecimalFormat df = new DecimalFormat("#.00");  
        int i=0;    
        for(i=0;i<10;i++){    
            n=sc.nextFloat();  
            if(n>max)max=n;    
            if(n<min)min=n;    
        }    
        System.out.println("maximum:"+df.format(max));  
        System.out.println("minimum:"+df.format(min));  
    }  
}  