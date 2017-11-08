import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner input=new Scanner(System.in);
        int num=input.nextInt();
        for(int i=0;i<num;i++){
            int n1=input.nextInt();
            int n2=input.nextInt();
            String ans="";
            for(int j=n1;j<=n2;j++){
                if((j+"").equals(reverse((j+"")))){
                    ans+=j+" ";
                }
            }
            if(!ans.equals(""))
                System.out.println(ans.substring(0,ans.length()-1));
            else
                System.out.println("0");
        }
    }
    public static String reverse(String originalStr){

String resultStr = "";

for(int i = originalStr.length() - 1 ; i >= 0 ; i--){

resultStr = resultStr + originalStr.charAt(i);

}

return resultStr; 

}

}


