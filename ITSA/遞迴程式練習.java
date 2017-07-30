import java.util.*;     
public class Main {     
    public static void main(String[] args) {     
        Scanner scn = new Scanner(System.in); 
        System.out.println(f(scn.nextInt()));
    }      
    public static int f(int n){
	if(n==1 || n==0)
            return n+1;
	else
            return (f(n-1)+f(n/2));	
    }
}  