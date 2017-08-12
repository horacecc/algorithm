import java.util.*;    
public class Main{    
    public static void main(String[] args){    
        Scanner cin = new Scanner(System.in);
        int ii=cin.nextInt();
        for(int i=0;i<ii;i++){
            int month=cin.nextInt();   
            if(month/3==1){    
                System.out.println("Spring");    
            }else if(month/3==2){    
                System.out.println("Summer");    
            }else if(month/3==3){    
                System.out.println("Autumn");    
            }else{    
                System.out.println("Winter");    
            } 
        }       
    }     
}  