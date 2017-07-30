import java.io.*;
public class Main{
    public static void main(String args[]) throws Exception{
        String getbr;
        int a,b;
        BufferedReader br= new BufferedReader(new InputStreamReader(System.in));
        getbr = br.readLine();
        if (getbr.length()!=10){
            System.out.println("WRONG!!!");
            return;
        }
        a=0;
        getbr =getbr.toUpperCase();
        if (getbr.charAt(0)=='A') a=10;
        else if (getbr.charAt(0)=='B') a=11;
        else if (getbr.charAt(0)=='C') a=12;
        else if (getbr.charAt(0)=='D') a=13;
        else if (getbr.charAt(0)=='E') a=14;
        else if (getbr.charAt(0)=='F') a=15;
        else if (getbr.charAt(0)=='G') a=16;
        else if (getbr.charAt(0)=='H') a=17;
        else if (getbr.charAt(0)=='I') a=34;
        else if (getbr.charAt(0)=='J') a=18;
        else if (getbr.charAt(0)=='K') a=19;
        else if (getbr.charAt(0)=='L') a=20;
        else if (getbr.charAt(0)=='M') a=21;
        else if (getbr.charAt(0)=='N') a=22;
        else if (getbr.charAt(0)=='O') a=35;
        else if (getbr.charAt(0)=='P') a=23;
        else if (getbr.charAt(0)=='Q') a=24;
        else if (getbr.charAt(0)=='R') a=25;
        else if (getbr.charAt(0)=='S') a=26;
        else if (getbr.charAt(0)=='T') a=27;
        else if (getbr.charAt(0)=='U') a=28;
        else if (getbr.charAt(0)=='V') a=29;
        else if (getbr.charAt(0)=='W') a=30;
        else if (getbr.charAt(0)=='X') a=31;
        else if (getbr.charAt(0)=='Y') a=32;
        else if (getbr.charAt(0)=='Z') a=33;
        else{
            System.out.println("WRONG!!!");
            return;
        }
        a=(a%10)*9+a/10;
        b=0;
        if ((getbr.charAt(1)-'0')!=1&&(getbr.charAt(1)-'0')!=2){
            System.out.println("WRONG!!!");
            return;
        }
        b=(getbr.charAt(1)-'0')*8+
        (getbr.charAt(2)-'0')*7+
        (getbr.charAt(3)-'0')*6+
        (getbr.charAt(4)-'0')*5+
        (getbr.charAt(5)-'0')*4+
        (getbr.charAt(6)-'0')*3+
        (getbr.charAt(7)-'0')*2+
        (getbr.charAt(8)-'0')*1;
        a=a+b;
        a=10-a%10;
        if (a>=10)a=0;
        if (getbr.charAt(9)-'0'==a)
            System.out.println("CORRECT!!!");
        else
            System.out.println("WRONG!!!");
    }
}