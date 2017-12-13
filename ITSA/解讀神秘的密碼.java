import java.util.Scanner;
public class Main {
    public static void main(String[] arg){
        Scanner sc = new Scanner(System.in);
	int nn= sc.nextInt();
        sc.nextLine();
	for(int i=0;i<nn;i++){
           String sec = sc.nextLine();
           for(int j=sec.length()-1;j>=0;j--){
               System.out.print(sec.substring(j,j+1));
           }
           System.out.println();
        }
    }
}