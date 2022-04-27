package JAVA;
import java.util.Scanner;

public class Fatorial {

    public static void main(String[] args) {
        
        Scanner s = new Scanner(System.in);
        System.out.println("Digite o valor de N:");
        int n = Integer.parseInt(s.next());
        int fatorial = 1;
        for (int i = 1; i <= n; i++) {
            fatorial = fatorial * i;           
        }
        System.out.println("Fatorial: "+fatorial);
        s.close();
    }
}
