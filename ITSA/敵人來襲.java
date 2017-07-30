import java.util.*;  
public class Main {  
    public static void main(String[] args) {  
        Scanner scn = new Scanner(System.in); 
        int cou=scn.nextInt();
        for(int i=0;i<cou;i++){
            int N=scn.nextInt(),S=scn.nextInt();
            if(S==4){
                for(int j=0;j<N;j++){
                    System.out.print("*");
                    for(int k=0;k<N-1;k++){
                        System.out.print(" x");
                    }  
                    System.out.println();
                }
            }else if(S==3){
                for(int j=0;j<N;j++){
                    for(int k=0;k<N-1;k++){
                        System.out.print("x ");
                    }  
                    System.out.print("*");
                    System.out.println();
                }
            }else if(S==2){
                for(int j=0;j<N;j++){
                    for(int k=0;k<N;k++){
                        if(j==k)
                            System.out.print("*");
                        else
                            System.out.print("x");
                        if(k!=N-1)
                            System.out.print(" ");
                    }  
                    System.out.println();
                }
            }else if(S==1){
                for(int j=0;j<N;j++){
                    for(int k=0;k<N;k++){
                        if(k==(N-j-1))
                            System.out.print("*");
                        else
                            System.out.print("x");
                        if(k!=N-1)
                            System.out.print(" ");
                    }  
                    System.out.println();
                }
            }
        }
    }  
}  