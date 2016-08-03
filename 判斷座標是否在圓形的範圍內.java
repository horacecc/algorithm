import java.util.*;    
public class Main {  
    public static void main(String[] args) {  
        Scanner cin = new Scanner(System.in);    
        int input1 = cin.nextInt();  
        int input2 = cin.nextInt();  
        if(input1>=-100&&input1<=100&&input2>=-100&&input2<=100)  
            System.out.println("inside");  
        else  
            System.out.println("outside");  
    }      
}  