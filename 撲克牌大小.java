import java.util.*;
public class Main {
    public static void main(String[] args) {
	Scanner scn = new Scanner(System.in);
	int n = Integer.parseInt(scn.nextLine());
	while (n-- != 0) {
            String str = scn.nextLine(), s[] = str.split(" "), arr[][] = new String[s.length][2];
            for (int i = 0; i < s.length; i++) {
                arr[i][0] = s[i].substring(0, 1);
		arr[i][1] = s[i].substring(1);
            }
            for (int i = 0; i < arr.length - 1; i++) {
		for (int j = i + 1; j < arr.length; j++) {
                    char c1[] = arr[i][0].toCharArray();
                    char c2[] = arr[j][0].toCharArray();
                    if (c1[0] == c2[0]) {
			int n1 = Integer.parseInt(arr[i][1]), n2 = Integer.parseInt(arr[j][1]);
			if (n1 < n2) {
                            String temp = arr[i][0];
                            arr[i][0] = arr[j][0];
                            arr[j][0] = temp;
                            temp = arr[i][1];
                            arr[i][1] = arr[j][1];
                            arr[j][1] = temp;
			}
                    }else if (c1[0] < c2[0]) {
			String temp = arr[i][0];
                        arr[i][0] = arr[j][0];
			arr[j][0] = temp;
			temp = arr[i][1];
			arr[i][1] = arr[j][1];
			arr[j][1] = temp;
                    }
		}
            }
            for (int i = 0; i < arr.length; i++) {
                if (i != 0)
                    System.out.print(" ");
		System.out.print(arr[i][0] + arr[i][1]);
            }
            System.out.println();
	}
    }
}