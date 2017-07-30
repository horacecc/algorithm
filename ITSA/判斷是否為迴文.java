import java.util.Scanner;      
public class Main{      
    public static void main(String args[]){      
       Scanner scn = new Scanner(System.in);      
       while(scn.hasNext()){    
           String st = scn.nextLine();    
           String st1 = "";    
           for(int a=st.length()-1;a>=0;a--){    
               st1 += st.charAt(a);    
           }    
           if(st1.equals(st))    
               System.out.println("YES");    
           else    
               System.out.println("NO");    
       }    
    }         
}  