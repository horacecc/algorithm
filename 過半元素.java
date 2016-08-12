import java.util.*;    
public class Main {    
    public static void main(String[] args) {    
        Scanner scn = new Scanner(System.in);    
        while(scn.hasNext()){  
            String arr[]=scn.nextLine().split(" ");  
            int i=0;  
            for(i=0;i<arr.length;i++){  
                int count=0;  
                for(int j=0;j<arr.length;j++){  
                    if(arr[i].equals(arr[j]))  
                        count++;  
                }  
                if(arr.length/2<count){  
                    System.out.println(arr[i]);  
                    break;  
                }  
            }  
            if(i==arr.length)  
                System.out.println("NO");  
        }  
    }  
} 