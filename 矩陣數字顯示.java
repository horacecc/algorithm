import java.util.*;    
public class Main {  
    public static void main(String[] args) {  
          
        Scanner cin = new Scanner(System.in);    
        String input = cin.next();  
          
        String[][] str={  
                        {"*****","    *","*****","*****","*   *","*****","*    ","*****","*****","*****"},  
                        {"*   *","    *","    *","    *","*   *","*    ","*    ","    *","*   *","*   *"},  
                        {"*   *","    *","*****","*****","*****","*****","*****","    *","*****","*****"},  
                        {"*   *","    *","*    ","    *","    *","    *","*   *","    *","*   *","    *"},  
                        {"*****","    *","*****","*****","    *","*****","*****","    *","*****","    *"}  
                       };  
          
        for(int j=0;j<5;j++){  
            for(int i=0;i<input.length();i++){  
                System.out.print(str[j][Integer.parseInt(input.substring(i, i+1))]);  
                if(i!=input.length()-1)  
                    System.out.print(" ");  
            }  
            System.out.println("");  
        }  
  
          
          
    }      
}  