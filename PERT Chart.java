import java.util.*;  
public class Main {  
    static int max;
    static String[] st1;
    static String[] st2;
    static int[] in;
    static int count;
    public static void main(String[] args) {  
        Scanner scn = new Scanner(System.in); 
        int cou=scn.nextInt();
        for(int i=0;i<cou;i++){
            max=0;
            st1=new String[200];
            st2=new String[200];
            in=new int[200];
            count=0;
            while(scn.hasNext()){
                String s1=scn.nextLine();
                if(s1.equals("end"))
                    break;
                if(!s1.equals("case")&&!s1.equals("")){
                    String[] sr2=s1.split(" ");
                    st1[count]=sr2[0];
                    st2[count]=sr2[1];
                    in[count]=Integer.parseInt(sr2[2]);
                    count++;
                }
            }
            ans("initial",0);
            System.out.println(max);       
        }
    }
    public static void ans(String next ,int value){
        if(next.equals("terminal")){
            if(max<value){
                max=value;
            }
        }else{
            for(int i=0;i<count;i++)
                if(next.equals(st1[i])){
                    ans(st2[i],value+in[i]);
                }  
        } 
    }    
}  