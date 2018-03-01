import java.util.Scanner;
public class Main {
    public static void main(String[] arg){
        Scanner sc = new Scanner(System.in);
	int num= sc.nextInt();
        int[] dollor=new int[]{1,5,10,50};
        sc.nextLine();
        for(int i=0;i<num;i++){
            String input =sc.nextLine();
            int total=0;
            String[] inputArray=input.split(",");
            if(inputArray[1].equals("1")){
                total=Integer.parseInt(inputArray[0])-Integer.parseInt(inputArray[2])*17;
            }else{
                total=Integer.parseInt(inputArray[0])-Integer.parseInt(inputArray[2])*25;
            }
            int[] count=new int[dollor.length];
            for(int j=count.length-1;j>-1;j--){
                while(total/dollor[j]>0){
                    total-=dollor[j];
                    count[j]++;
                }
            }
            String str="";
            for(int j=0;j<count.length;j++){
                if(count[j]!=0)
                    str+="Coin "+dollor[j]+":"+count[j]+",";
            }
            System.out.println(str.substring(0,str.length()-1));
        }         
    }
}