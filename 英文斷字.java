import java.util.*;  
   
public class Main {  
   
    public static void main(String[] args) {  
        Scanner scn = new Scanner(System.in); 
        int cou=scn.nextInt();
        for(int ii=0;ii<=cou;ii++){
            String str = scn.nextLine().toLowerCase(), arr[] = str.split(" ");
            if(ii!=0){
            int i = 0, j = 0;  
            System.out.print(arr[0] + " ");  
            for (i = 1; i < arr.length; i++) {  
                for (j = i - 1; j >= 0; j--) {  
                    if (arr[j].equals(arr[i]))  
                        break;  
                }  
                if (j == -1) {  
                    if (i != 1)  
                        System.out.print(" ");  
                    System.out.print(arr[i].toLowerCase());  
                }  
            }  
            System.out.println();
            }  
        }
    }  
}  