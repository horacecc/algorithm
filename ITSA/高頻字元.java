import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner input=new Scanner(System.in);
        int num=input.nextInt();
        input.nextLine();
        for(int i=0;i<num;i++){
            String str=input.nextLine();
            String[] st=str.split("");
            String max="";
            int maxInt=0;
            for(int j=0;j<st.length-1;j++){
                int nextMaxInt=0;
                for(int k=j+1;k<st.length;k++){
                    if(st[j].equals(st[k])){
                        nextMaxInt++;
                    }
                }   
                if(nextMaxInt>maxInt){
                    max=st[j];
                    maxInt=nextMaxInt;
                }
            }
            System.out.println(max);
        }  
        
    }
}
