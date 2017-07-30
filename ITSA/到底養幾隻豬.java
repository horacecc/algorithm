import java.util.*;  
public class Main {  
    public static void main(String[] args) {  
        Scanner scn = new Scanner(System.in); 
        int cou=scn.nextInt();
        for(int i=0;i<cou;i++){
            int a=scn.nextInt(),b=scn.nextInt(),c=scn.nextInt(),ans=0;
            for(int j=0;j<2147483647;j++){
                ans=7*j+a;
                if((ans+b)%11==0&&(ans-c)%17==0){
                    System.out.println(ans);
                    break;
                }
            }
        }
    }  
}  