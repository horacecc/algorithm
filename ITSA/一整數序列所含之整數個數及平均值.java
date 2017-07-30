import java.util.Scanner; 
public class Main{ 
    public static void main(String[] args){ 
        Scanner scn = new Scanner(System.in); 
        while(scn.hasNextLine()){ 
            String str=scn.nextLine(); 
            String[] n=str.split(" "); 
            System.out.println("Size: "+n.length);  
            System.out.println("Average: "+sum(n)); 
        } 
    } 
    public static String sum(String[] n){ 
        double ans=0; 
        for(int i=0;i<n.length;i++) 
            ans+=Integer.parseInt(n[i]); 
        return ((Math.round(ans*1000/n.length)+"").substring(0,((Math.round(ans*1000/n.length)+"")).length()-3))+"."+((Math.round(ans*1000/n.length)+"").substring(((Math.round(ans*1000/n.length))+"").length()-3)); 
    } 
}  