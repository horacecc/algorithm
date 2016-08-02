import java.util.*;    
     
public class Main {    
     
    public static void main(String[] args) {    
        Scanner scn = new Scanner(System.in);    
        int n=scn.nextInt();    
        if(n<0)n+=256;    
        int arr[]=new int [8];    
        for(int i=7;i>=0;i--){    
            arr[i]=n%2;    
            n/=2;    
        }    
        for(int i:arr)    
            System.out.print(i);    
        System.out.println();    
    }    
}  