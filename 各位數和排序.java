import java.util.*;     
public class Main {     
 public static void main(String[] args) {     
       Scanner scn=new Scanner (System.in);     
       while(scn.hasNext()){     
          int n=scn.nextInt(),i=0,sort[][]=new int [n][2],temp=0;     
            for(;i<n;i++){     
          int tot=0,num=scn.nextInt();     
           sort[i][0]=num;     
            while(num!=0){     
             tot+=num%10;     
               num/=10;     
           }     
          sort[i][1]=tot;     
            }     
          for(i=0;i<n-1;i++){     
             for(int j=0;j<n-i-1;j++){     
                   if(sort[j][1]==sort[j+1][1]){     
                      if(sort[j][0]>sort[j+1][0]){     
                            temp=sort[j+1][0];     
                         sort[j+1][0]=sort[j][0];     
                           sort[j][0]=temp;     
                           temp=sort[j+1][1];     
                         sort[j+1][1]=sort[j][1];     
                           sort[j][1]=temp;     
                       }     
                  }     
                  if(sort[j][1]>sort[j+1][1]){     
                        temp=sort[j+1][0];     
                     sort[j+1][0]=sort[j][0];     
                       sort[j][0]=temp;     
                       temp=sort[j+1][1];     
                     sort[j+1][1]=sort[j][1];     
                       sort[j][1]=temp;     
                   }     
              }     
          }     
          for(i=0;i<n;i++){     
               System.out.print(sort[i][0]);     
              if(i<n-1)System.out.print(" ");     
         }     
          System.out.printf("\n");     
       }     
 }      
}  