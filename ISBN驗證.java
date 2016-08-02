import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner scn = new Scanner(System.in);
        int ans1=0,ans2=0;
        for(int i=0;i<10;i++){
            String str=scn.next();
            int intValue=10;
            if(!str.equals("X"))
                intValue  = Integer.parseInt(str);            
            ans1+=intValue;
            ans2+=ans1;
        }
        if(ans2%11==0)
            System.out.println("YES");
        else
            System.out.println("NO");
    }
}