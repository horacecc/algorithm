import java.util.Arrays;
import java.util.Scanner;
public class Main {
    public static int lenNum(int i,int j){
        return j-i+1;
    }
    public static int ansNum(int ii,int jj,int[] s1,int[] s2,int tmpo){
        //System.out.print("tmpo¡G"+tmpo+",ii="+ii+",jj="+jj);
        int fristNum=-1,LastNum=-1;
        for(int j=s1.length-1;j>=0;j--){
            if(s1[j]<=ii){
                if(fristNum!=-1){
                    if(lenNum(s1[fristNum],s2[fristNum])<lenNum(s1[j],s2[j])){
                        fristNum=j;
                    }
                }else{
                    fristNum=j;
                }
            }
        }
        for(int j=s1.length-1;j>=0;j--){
            if(fristNum==-1){
                break;
            }
            if(s2[fristNum]>=jj){
                LastNum=fristNum;
                break;
            }
            if(s2[j]>=jj){
                if(LastNum!=-1){
                    if(lenNum(s1[LastNum],s2[LastNum])<lenNum(s1[j],s2[j])){
                        LastNum=j;
                    }
                }else{
                    LastNum=j;
                }
            }
        }
        //System.out.print(",fristNum="+fristNum);
        //System.out.print(",LastNum="+LastNum);
        if(fristNum==-1||LastNum==-1){
            //System.out.println(",return="+(-1));
            return -1;
        }else if(fristNum==LastNum){
            //System.out.println(",return="+(1));
            return 1;
        }else if(s1[fristNum]>=s2[LastNum]){
            //System.out.println(",return="+(2));
            return 2;
        }else{
            
            int[] s1Remove = new int[s1.length - 2];
            int[] s2Remove = new int[s2.length - 2];
            int count = 0; 
            for (int iii = 0; iii < s1.length; iii++) {
                if (iii != fristNum && iii!=LastNum) {
                    s1Remove[count]=s1[iii];
                    s2Remove[count]=s2[iii];       
                    count++;
                }
            }
            if(s2[fristNum]==s1[LastNum]){
                return 2;
            }
            int anss=ansNum(s2[fristNum],s1[LastNum],s1Remove,s2Remove,++tmpo);
            if(anss==-1){
                //System.out.println(",return="+(-1));
               return -1; 
            }else{
               // System.out.println(",return="+(2+anss));
               return 2+anss;
            }               
        }
    }
    public static void main(String[] arg){
        Scanner sc = new Scanner(System.in);
	int nn= sc.nextInt();
        sc.nextLine();
	for(int i=0;i<nn;i++){
            int N=sc.nextInt()-1;
            int M=sc.nextInt();
            int[] s1=new int[M];
            int[] s2=new int[M];
            for(int j=0;j<s1.length;j++){
                s1[j]=sc.nextInt();
            }            
            for(int j=0;j<s2.length;j++){
                s2[j]=sc.nextInt();
            }
            
            String[] strArray=new String[M];
            for(int j=0;j<s1.length;j++){
                strArray[j]=s1[j]+"/"+s2[j];
            }
            Arrays.sort(strArray);
            s1=new int[M];
            s2=new int[M];
            for(int j=0;j<s1.length;j++){
                String[] gg=strArray[j].split("/");
                s1[j]=Integer.parseInt(gg[0]);
                s2[j]=Integer.parseInt(gg[1]);
            }  
            System.out.println(ansNum(0,N,s1,s2,1));           
        }
    }
}