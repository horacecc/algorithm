import java.util.*;  
public class Main {  
    public static void main(String[] args) {  
        Scanner scn = new Scanner(System.in); 
        String[] cou_array = scn.nextLine().split(",");
        if((Integer.parseInt(cou_array[1])*15+Integer.parseInt(cou_array[2])*20+Integer.parseInt(cou_array[3])*30)>Integer.parseInt(cou_array[0]))
            System.out.println("0");
        else
           System.out.println(((Integer.parseInt(cou_array[0])-(Integer.parseInt(cou_array[1])*15+Integer.parseInt(cou_array[2])*20+Integer.parseInt(cou_array[3])*30))-(((Integer.parseInt(cou_array[0])-(Integer.parseInt(cou_array[1])*15+Integer.parseInt(cou_array[2])*20+Integer.parseInt(cou_array[3])*30))-((Integer.parseInt(cou_array[0])-(Integer.parseInt(cou_array[1])*15+Integer.parseInt(cou_array[2])*20+Integer.parseInt(cou_array[3])*30))/50)*50)/5)*5-((Integer.parseInt(cou_array[0])-(Integer.parseInt(cou_array[1])*15+Integer.parseInt(cou_array[2])*20+Integer.parseInt(cou_array[3])*30))/50)*50)+","+(((Integer.parseInt(cou_array[0])-(Integer.parseInt(cou_array[1])*15+Integer.parseInt(cou_array[2])*20+Integer.parseInt(cou_array[3])*30))-((Integer.parseInt(cou_array[0])-(Integer.parseInt(cou_array[1])*15+Integer.parseInt(cou_array[2])*20+Integer.parseInt(cou_array[3])*30))/50)*50)/5)+","+((Integer.parseInt(cou_array[0])-(Integer.parseInt(cou_array[1])*15+Integer.parseInt(cou_array[2])*20+Integer.parseInt(cou_array[3])*30))/50)); 
    }  
}  