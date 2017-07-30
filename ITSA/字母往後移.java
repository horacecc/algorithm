import java.util.Scanner;
public class Main {
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        String str=sc.nextLine();
        int n=sc.nextInt();
        for(int i=0;i<str.length();i++){
            char ch=str.charAt(i);
            int num=(int)ch;
            if(num>=48&&num<=57){
                num+=n;
                num=num>57?num-10:num;
            }else if(num>=65&&num<=90){
                num+=n;
                num=num>90?num-26:num;
            }else if(num>=97&&num<=122){
                num+=n;
                num=num>122?num-26:num;
            }
            System.out.print((char)num);
        }
        System.out.println();
    }
}