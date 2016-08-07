import java.util.*;    
public class Main    
{    
    public static void main(String[] args)    
    {    
        Scanner cin = new Scanner(System.in);    
        int n1,n2;    
        n1=((cin.nextInt()*60+cin.nextInt())-(cin.nextInt()*60+cin.nextInt()))*-1;    
        if(n1<121)    
        {    
            n2=n1-n1%30;    
        }else if(n1<241){    
            n2=120+(n1-n1%30-120)*4/3;    
        }else{    
            n2=280+(n1-n1%30-240)*6/3;    
        }    
        System.out.println(n2);    
    }     
}  