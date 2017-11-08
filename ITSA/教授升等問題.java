import java.util.*;
import java.text.DecimalFormat;
public class Main {
    public static void main(String[] args) {
        Scanner input=new Scanner(System.in);
        int num=input.nextInt();
        for(int i=0;i<num;i++){
            double W=input.nextDouble();
            double P=input.nextDouble();
            double[] wArray=new double[]{input.nextDouble(),input.nextDouble(),input.nextDouble()};
            double[] pArray=new double[]{input.nextDouble(),input.nextDouble(),input.nextDouble()};
            
            double ans1=0,ans2=0;
            int ans3=0,ans4=0,A=0,B=0,C=0;
            
            
            for(int j=0;j<((W/wArray[0])+1);j++){
                for(int k=0;k<((W/wArray[1])+1);k++){
                    for(int l=0;l<((W/wArray[2])+1);l++){
                        if((j*wArray[0]+k*wArray[1]+l*wArray[2])<=W && (j*pArray[0]+k*pArray[1]+l*pArray[2])>=P){
                            
                            if(ans1<(j*pArray[0]+k*pArray[1]+l*pArray[2])){
                                ans1=(j*pArray[0]+k*pArray[1]+l*pArray[2]);
                                ans2=(W-(j*wArray[0]+k*wArray[1]+l*wArray[2]));
                                if(pArray[0]==Math.max(pArray[2],Math.max(pArray[0],pArray[1])))
                                    ans3=j;
                                else if(pArray[1]==Math.max(pArray[2],Math.max(pArray[0],pArray[1])))
                                    ans3=k;
                                else
                                    ans3=l;
                                
                                ans4=j+k+l;
                                A=j;
                                B=k;
                                C=l;
                            }else if(ans1==(j*pArray[0]+k*pArray[1]+l*pArray[2])){
                                if(ans2<(W-(j*wArray[0]+k*wArray[1]+l*wArray[2]))){
                                    ans1=(j*pArray[0]+k*pArray[1]+l*pArray[2]);
                                    ans2=(W-(j*wArray[0]+k*wArray[1]+l*wArray[2]));
                                    if(pArray[0]==Math.max(pArray[2],Math.max(pArray[0],pArray[1])))
                                        ans3=j;
                                    else if(pArray[1]==Math.max(pArray[2],Math.max(pArray[0],pArray[1])))
                                        ans3=k;
                                    else
                                        ans3=l;

                                    ans4=j+k+l;
                                    A=j;
                                    B=k;
                                    C=l;
                                }else if(ans2==(W-(j*wArray[0]+k*wArray[1]+l*wArray[2]))){
                                    int tmp=0;
                                    if(pArray[0]==Math.max(pArray[2],Math.max(pArray[0],pArray[1])))
                                        tmp=j;
                                    else if(pArray[1]==Math.max(pArray[2],Math.max(pArray[0],pArray[1])))
                                        tmp=k;
                                    else
                                        tmp=l;
                                    if(ans3<tmp){
                                        ans1=(j*pArray[0]+k*pArray[1]+l*pArray[2]);
                                        ans2=(W-(j*wArray[0]+k*wArray[1]+l*wArray[2]));
                                        if(pArray[0]==Math.max(pArray[2],Math.max(pArray[0],pArray[1])))
                                            ans3=j;
                                        else if(pArray[1]==Math.max(pArray[2],Math.max(pArray[0],pArray[1])))
                                            ans3=k;
                                        else
                                            ans3=l;

                                        ans4=j+k+l;
                                        A=j;
                                        B=k;
                                        C=l;
                                    }else if(ans3==tmp){
                                        if(ans4<(j+k+l)){
                                            ans1=(j*pArray[0]+k*pArray[1]+l*pArray[2]);
                                            ans2=(W-(j*wArray[0]+k*wArray[1]+l*wArray[2]));
                                            if(pArray[0]==Math.max(pArray[2],Math.max(pArray[0],pArray[1])))
                                                ans3=j;
                                            else if(pArray[1]==Math.max(pArray[2],Math.max(pArray[0],pArray[1])))
                                                ans3=k;
                                            else
                                                ans3=l;

                                            ans4=j+k+l;
                                            A=j;
                                            B=k;
                                            C=l;
                                        }
                                    }
                                }
                            }
                            
                            
                            
                            
                            //System.out.println(j+"\t"+k+"\t"+l+"\t"+(W-(j*wArray[0]+k*wArray[1]+l*wArray[2]))+"\t"+(j*pArray[0]+k*pArray[1]+l*pArray[2]));
                        }
                    }
                }
            }
            DecimalFormat df = new DecimalFormat("0.000");
            if(ans1==0)
                System.out.println("0");
            else
                System.out.println(A+" "+B+" "+C+" "+df.format(ans1)+" "+df.format(ans2));
        }
    }
}

/*2
5 10 1.0 1.0 1.0 2.1 1.9 1.8
4 10 1.2 1.2 1.0 2.1 2.4 2.1*/