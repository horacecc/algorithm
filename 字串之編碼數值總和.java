import java.util.*;  
public class Main {  
    public static void main(String[] args) {  
        Scanner scn = new Scanner(System.in);  
        int n=Integer.parseInt(scn.nextLine());
        while(n--!=0){
            char arr[]=scn.nextLine().toCharArray();
            int tot=0;
            for(int i=0;i<arr.length;i++){
                tot+=arr[i];
            }
            System.out.println(tot);
        }
    }
} 