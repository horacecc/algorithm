import java.util.*;    
public class Main{    
    public static void main(String[] args){    
        Scanner cin = new Scanner(System.in);
        int m=cin.nextInt();
        cin.nextLine();
        for(int i=0;i<m;i++){   
            String[] n2_array=cin.nextLine().split(" ");
            int total=Integer.parseInt(n2_array[n2_array.length-1]);
            int[] money=new int[n2_array.length-1],money_count=new int[n2_array.length-1];
            int count=2147483647;
            
            
            
            for(int j=0;j<money.length;j++){
                money[j]=Integer.parseInt(n2_array[j]);
            }
            
            for(int m3=0;m3<=(total/money[3]);m3++){
                for(int m2=0;m2<=(total/money[2]);m2++){
                    for(int m1=0;m1<=(total/money[1]);m1++){
                        for(int m0=0;m0<=(total/money[0]);m0++){
                            
                            if((money[0]*m0+money[1]*m1+money[2]*m2+money[3]*m3)==total)
                                if((m0+m1+m2+m3)<count){
                                    System.out.println((m0+"\t"+m1+"\t"+m2+"\t"+m3));
                                    count=(m0+m1+m2+m3);
                                    money_count[0]=m0;
                                    money_count[1]=m1;
                                    money_count[2]=m2;
                                    money_count[3]=m3;
                                    money_count[4]=total-(m0+m1+m2+m3);
                                }                           
                        } 
                    } 
                } 
            } 
            System.out.println(count+money_count[4]);
            for(int j=0;j<money.length;j++)
                System.out.println(money[j]+" "+money_count[j]);
        }       
    }     
}  