import java.util.Scanner; 
public class Main{ 
    public static void main (String [] argv){ 
        Scanner input = new Scanner(System.in); 
        int num = input.nextInt(); 
        input.nextLine(); 
        for(int i =0 ;i<num;i++){
            String month = input.nextLine(); 
            String[] ss=month.split("");
            int nn=10;
            for(int j=0;j<ss.length;j++){
                if(ss[j].equals("(")){
                    nn++;
                }else{
                    nn--;
                }
            }
            if(nn==10){
                System.out.println("Yes");
            }else{
                System.out.println("No");
            }
        }
    } 
} 