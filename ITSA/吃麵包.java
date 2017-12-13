import java.util.Scanner;
public class Main {
    public static void main(String[] arg){
        Scanner sc = new Scanner(System.in);
	int nn= sc.nextInt();
	for(int i=0;i<nn;i++){
            int n1 = sc.nextInt();
            int n2 = sc.nextInt();
            int[] mb=new int[n1]; 
            for(int j=0;j<n1;j++){
                mb[j]=sc.nextInt();
            }
            for(int j=0;j<n2;j++){
                int n3 = sc.nextInt()-1;
                int n4 = sc.nextInt();
                int sum=0;
                for(int k=n3;k<n4;k++){
                    sum+=mb[k];
                }
                System.out.println(sum);
            }
        }
    }
}