import java.util.Scanner; 
import java.text.DecimalFormat;
public class Main{ 
    public static void main (String [] argv){ 
        Scanner input = new Scanner(System.in); 
        while(input.hasNext()){
            String[] str=input.nextLine().split("");
            int ss=0;
            int count=0;
            for(int i=0;i<str.length-1;i++){
                if(!str[i].equals("-")){
                    count++;
                    ss+=Integer.parseInt(str[i])*count;
                }                
            }
            if(ss%11==Integer.parseInt(str[str.length-1])){
                System.out.println("Pass");
            }else{
                System.out.println("Fail");
            }
        }
    } 
} 
