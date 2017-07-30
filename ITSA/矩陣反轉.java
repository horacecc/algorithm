import java.util.*;      
    
public class Main {      
    public static void main(String[] args){      
        Scanner cin = new Scanner(System.in);      
        while(cin.hasNext()) {    
            int a=cin.nextInt(),b=cin.nextInt(),count=0;    
            int[] box=new int[a*b];  
            for(int i=0;i<(a*b);i++){    
                box[i]=cin.nextInt();  
            }    
            for(int y=0;y<b;y++){    
                for(int x=0;x<a;x++){    
                    count++;  
                    System.out.print(box[x*b+y]);    
                    if(count%a!=0){    
                        System.out.print(" ");   
                    }    
                }    
                System.out.println();  
            }    
        }    
    }       
}  