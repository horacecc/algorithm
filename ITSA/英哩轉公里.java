import java.util.*;    
public class Main {  
    public static void main(String[] args) {  
          
        Scanner cin = new Scanner(System.in);    
        int input = cin.nextInt();  
        System.out.println(Math.round(input*16)/10+"."+Math.round(input*16)%10);  
    }      
}  