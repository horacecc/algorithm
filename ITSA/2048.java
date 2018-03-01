import java.util.Scanner;
public class Main {
    public static void arr0s(String to){
            for(int ll=0;ll<30;ll++){
                if(to.equals("U")){
                    for(int j=0;j<4;j++){
                        for(int k=0;k<3;k++){
                            if(array[k*4+j]==0&&array[(k+1)*4+j]!=0){
                                array[k*4+j]=array[(k+1)*4+j];
                                array[(k+1)*4+j]=0;
                            }
                        }
                    }
                }else if(to.equals("D")){
                    for(int j=3;j>-1;j--){
                        for(int k=3;k>0;k--){
                            if(array[k*4+j]==0&&array[(k-1)*4+j]!=0){
                                array[k*4+j]=array[(k-1)*4+j];
                                array[(k-1)*4+j]=0;
                            }
                        }
                    }
                }else if(to.equals("L")){
                    for(int k=0;k<3;k++){
                        for(int j=0;j<4;j++){
                            if(array[k+j*4]==0&&array[k+j*4+1]!=0){
                                array[k+j*4]=array[k+j*4+1];
                                array[k+j*4+1]=0;
                            }
                        }
                    }
                }else if(to.equals("R")){
                    for(int k=3;k>0;k--){
                        for(int j=3;j>-1;j--){
                            if(array[k+j*4]==0&&array[k+j*4-1]!=0){
                                array[k+j*4]=array[k+j*4-1];
                                array[k+j*4-1]=0;
                            }
                        }
                    }
                }
            }
    }
    static int[] array;
    public static void main(String[] arg){
        Scanner sc = new Scanner(System.in);
	int num= Integer.parseInt(sc.next());
        for(int i=0;i<num;i++){
            String to = sc.next();
            array=new int[16];
            for(int j=0;j<array.length;j++){
                array[j]=Integer.parseInt(sc.next());
            }
arr0s(to);
                if(to.equals("U")){
                    for(int j=0;j<4;j++){
                        for(int k=0;k<3;k++){
                            if(array[k*4+j]==0&&array[(k+1)*4+j]!=0){
                                array[k*4+j]=array[(k+1)*4+j];
                                array[(k+1)*4+j]=0;
                            }else if(array[k*4+j]==array[(k+1)*4+j]&&array[k*4+j]!=0){
                                array[k*4+j]*=2;
                                array[(k+1)*4+j]=0;
                                arr0s(to);
                                k=0;
                            }
                        }
                    }
                }else if(to.equals("D")){
                    for(int j=3;j>-1;j--){
                        for(int k=3;k>0;k--){
                            if(array[k*4+j]==0&&array[(k-1)*4+j]!=0){
                                array[k*4+j]=array[(k-1)*4+j];
                                array[(k-1)*4+j]=0;
                            }else if(array[k*4+j]==array[(k-1)*4+j]&&array[k*4+j]!=0){
                                array[k*4+j]*=2;
                                array[(k-1)*4+j]=0;
                                arr0s(to);
                                k=3;
                            }
                        }
                    }
                }else if(to.equals("L")){
                    for(int j=0;j<4;j++){
                        for(int k=0;k<3;k++){
                            if(array[k+j*4]==0&&array[k+j*4+1]!=0){
                                array[k+j*4]=array[k+j*4+1];
                                array[k+j*4+1]=0;
                            }else if(array[k+j*4]==array[k+j*4+1]&&array[k+j*4]!=0){
                                array[k+j*4]*=2;
                                array[k+j*4+1]=0;
                                arr0s(to);
                                k=0;
                            }
                        }
                    }
                }else if(to.equals("R")){
                    for(int j=3;j>-1;j--){
                        for(int k=3;k>0;k--){
                            if(array[k+j*4]==0&&array[k+j*4-1]!=0){
                                array[k+j*4]=array[k+j*4-1];
                                array[k+j*4-1]=0;
                            }else if(array[k+j*4]==array[k+j*4-1]&&array[k+j*4]!=0){
                                array[k+j*4]*=2;
                                array[k+j*4-1]=0;
                                arr0s(to);
                                k=3;
                            }
                        }
                    }
                }
            
            
           
            for(int k=0;k<4;k++){
                for(int j=0;j<4;j++){
                    System.out.print(array[k*4+j]); 
                    if(j!=3){
                        System.out.print(" "); 
                    }
                }
                System.out.println(); 
            }
        }         
    }
}