import java.util.Scanner; 
import java.text.DecimalFormat;
public class Main{ 
    public static void main (String [] argv){ 
        Scanner input = new Scanner(System.in); 
        double[] num=new double[4];
        do{
            double[] num2=new double[3];
            num[0]=input.nextInt();
            num[1]=input.nextInt();
            num[2]=input.nextInt();
            num[3]=input.nextInt();
            
            num2[0]= (num[1] / num[0]) *41.2;
            num2[1]= (num[0] * num[1]) /634.4;
            num2[2]= (num[1]) *0.4;

            DecimalFormat df = new DecimalFormat("##.00");

            if(num[2]>30)
                num2[1]+=((num[2]-(num[2]%5))/5-6)*0.15;
            if(num[2]>28)
               num2[2]+=((num[2]-(num[2]%2))/2-14)*0.25;

      
            
            System.out.println(df.format(num2[0])+" "+df.format(num2[1])+" "+df.format(num2[2]));
        }while(num[3]!=-1);
    } 
} 
