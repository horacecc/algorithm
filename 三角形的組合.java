import java.util.*;  
public class Main {  
    public static void main(String[] args) {  
        Scanner scn = new Scanner(System.in); 
        int cou=scn.nextInt();
        for(int i=0;i<cou;i++){
            int m=scn.nextInt();
            String[] eng=new String[m];
            int[] len=new int[m];
            for(int j=0;j<m+1;j++){
                String sr=scn.nextLine();
                 if(j!=0){  
                    String[] sr2=sr.split(" ");
                    eng[j-1]=sr2[0];
                    len[j-1]=Integer.parseInt(sr2[1]);
                }
            }
            for(int j=0;j<m-2;j++){
                for(int k=j+1;k<m-1;k++){
                    if(j<k )
                    for(int l=j+2;l<m;l++){
                        if(k<l){
                            if((len[j]+len[k])>len[l]&&(len[j]-len[k])<len[l]&&(len[l]+len[k])>len[j]&&(len[l]-len[k])<len[j]&&(len[j]+len[l])>len[k]&&(len[j]-len[l])<len[k])
                                System.out.println(eng[j]+" "+eng[k]+" "+eng[l]);
                        }                        
                    }
                }
            }
        }
    }  
}  