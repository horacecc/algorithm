import java.util.*;    
public class Main{    
    public static void main(String[] args){    
        Scanner cin = new Scanner(System.in);
        int m=cin.nextInt();
        for(int i=0;i<m;i++){
            int n=cin.nextInt();
            String[] arr=new String[n];
            int total=0;
            for(int j=0;j<arr.length;j++){
                arr[j]=tenToTwo(cin.nextInt());
                arr[j]=String.format("%017d", Long.parseLong(arr[j]));
            }
            for(int j=16;j>=0;j--){
                int count=0;
                for(int k=0;k<arr.length;k++){
                    if(arr[k].substring(j,j+1).equals("1")){
                        count++;
                    }
                }
                if(count%2!=0)
                    total++;
            }
            /*System.out.println(total);*/
            if(total!=0)
                System.out.println("yes");
            else
                System.out.println("no");
        }       
    }   
    public static String tenToTwo(int input) { 
        if (input / 2 == 0) 
            return Integer.toString(input % 2); 
        return tenToTwo(input / 2) + (input % 2) ; 
    }  
}  