import java.util.Scanner; 
public class Main{ 
    public static void main (String [] argv){ 
        Scanner input = new Scanner(System.in); 
        int month = input.nextInt(); 
        int day = input.nextInt(); 
        String result=""; 
        switch(month){ 
            case 1: 
                if(day >=1 && day <=20) 
                    result="Capricorn"; 
                else if(day>=21 && day<=31) 
                    result="Aquarius"; 
            break; 
            case 2: 
                if(day >=1 && day <=19) 
                    result="Aquarius"; 
                else if(day>=20 && day<=29) 
                    result="Pisces"; 
            break; 
            case 3: 
                if(day >=1 && day <=20) 
                    result="Pisces"; 
                else if(day>=21 && day<=31) 
                    result="Aries"; 
            break; 
            case 4: 
                if(day >=1 && day <=20) 
                    result="Aries"; 
                else if(day>=21 && day<=30) 
                    result="Taurus"; 
            break; 
            case 5: 
                if(day >=1 && day <=21) 
                    result="Taurus"; 
                else if(day>=22 && day<=31) 
                    result="Gemini"; 
            break; 
            case 6: 
                if(day >=1 && day <=21) 
                    result="Gemini"; 
                else if(day>=22 && day<=30) 
                    result="Cancer"; 
            break; 
            case 7: 
                if(day >=1 && day <=23) 
                    result="Cancer"; 
                else if(day>=24 && day<=31) 
                    result="Leo"; 
            break; 
            case 8: 
                if(day >=1 && day <=23) 
                    result="Leo"; 
                else if(day>=24 && day<=31) 
                    result="Virgo"; 
            break; 
            case 9: 
                if(day >=1 && day <=23) 
                    result="Virgo"; 
                else if(day>=24 && day<=30) 
                    result="Libra"; 
            break; 
            case 10: 
                if(day >=1 && day <=23) 
                    result="Libra"; 
                else if(day>=24 && day<=31) 
                    result="Scorpio"; 
            break; 
            case 11: 
                if(day >=1 && day <=22) 
                    result="Scorpio"; 
                else if(day>=23 && day<=30) 
                    result="Sagittarius"; 
            break; 
            case 12: 
                if(day >=1 && day <=22) 
                    result="Sagittarius"; 
                else if(day>=23 && day<=31) 
                    result="Capricorn"; 
            break; 
        } 
        System.out.println(result); 
    } 
} 