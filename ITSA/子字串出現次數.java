import java.util.*;   
public class Main {   
public static void main(String args[]){   
Scanner s = new Scanner(System.in);   
    String str2 = s.nextLine();   
    String str1 = s.nextLine();   
int count=0;   
  
    for(int i=0;i<=str1.length()-str2.length();i++)   
     {   
     if(str2.equals(str1.substring(i, str2.length()+i)))   
       count++;   
       }   
System.out.println(count);   
}   
} 