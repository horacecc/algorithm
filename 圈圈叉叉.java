import java.util.*;  
  
public class Main {  
    public static void main(String[] args) {  
        Scanner sc=new Scanner(System.in);  
        int[][] arr=new int[3][3];  
        for(int i=0;i<3;i++)  
            for(int j=0;j<3;j++)  
                arr[i][j]=sc.nextInt();  
        boolean ok=false;  
        for (int i = 0; i < 3 && !ok; i++)  
    {  
        if (arr[i][0] == arr[i][1]  
            && arr[i][0] == arr[i][2])  
            ok = true;  
        if (arr[0][i] == arr[1][i]  
            && arr[0][i] == arr[2][i])  
            ok = true;  
    }  
      
    if (arr[0][0] == arr[1][1]  
        && arr[0][0] == arr[2][2])  
        ok = true;  
    if (arr[0][2] == arr[1][1]  
        && arr[0][2] == arr[2][0])  
        ok = true;  
  
    if (ok)  
            System.out.println("True");  
    else  
            System.out.println("False");  
    }  
}