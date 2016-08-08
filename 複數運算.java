import java.util.*;      
    
public class Main {      
    public static void main(String[] args){      
        Scanner cin = new Scanner(System.in);  
        int FQ=cin.nextInt(),a,b,a1,b1;  
        String c;  
        for(int i=0;i<FQ;i++){  
            c=cin.next();  
            a=cin.nextInt();  
            b=cin.nextInt();  
            a1=cin.nextInt();  
            b1=cin.nextInt();  
            if(c.equals("+"))  
                System.out.println((a+a1)+" "+(b+b1));  
            else if(c.equals("-")){  
                System.out.println((a-a1)+" "+(b-b1));  
            }else{  
                System.out.println((a*a1-b*b1)+" "+(b*a1+a*b1));  
            }  
        }  
    }       
}  