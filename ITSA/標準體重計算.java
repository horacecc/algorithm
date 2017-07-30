import java.util.*; 
import java.lang.*; 
import java.io.*; 
import java.util.InputMismatchException;
public class Main { 
    public static void main (String[] args) throws java.lang.Exception{ 
     int high, gender;   
        Scanner sc = new Scanner(System.in);
        for(int i = 0;i <100;i++){
            high = sc.nextInt();   
            gender = sc.nextInt();   
            if(gender == 1){   
                System.out.printf("%.1f", (long)(high-80 )*0.7);   
                System.out.println();
            }   
            if(gender == 2){   
                System.out.printf("%.1f", (long)(high-70)*0.6);   
                System.out.println();
            } 
        }
    } 
}