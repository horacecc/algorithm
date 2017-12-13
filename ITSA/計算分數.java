import java.util.Scanner;
public class Main {
    public static void main(String[] arg){
        Scanner sc = new Scanner(System.in);
	int nn= sc.nextInt();
        sc.nextLine();
	for(int i=0;i<nn;i++){
            String str=sc.nextLine();
            String[] Num=str.split(",");
            String[] r=Num[0].split("/");
            String[] l=Num[1].split("/");
            int up,down;
            up=Integer.parseInt(r[0])*Integer.parseInt(l[1])+Integer.parseInt(r[1])*Integer.parseInt(l[0]);
            down=Integer.parseInt(r[1])*Integer.parseInt(l[1]);
            
            
            
            System.out.println(up/f(up,down)+"/"+down/f(up,down));
        }
    }
    public static int f(int a,int b){  
        int count = 0;  
        for(int i=1;i<=Math.min(a, b);i++){  
            if(a%i==0&&b%i==0){  
                count = i;  
            }  
        }  
        return count;  
    }  
}