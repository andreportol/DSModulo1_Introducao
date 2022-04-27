package JAVA;
import java.util.Scanner;

public class ParesConsecutivos {
    public static void main(String[] args) {
        int x = 0, soma;
        Scanner s = new Scanner(System.in);
        do {
            System.out.print("Digite um numero inteiro: ");
            x = Integer.parseInt(s.next());
            if (x % 2 != 0 && x != 0) {
                x += 1;
            } 
            if (x != 0) {
                soma = 5 * x + 20;
                System.out.println("Soma: " + soma);
            }
        } while (x != 0);
        s.close();
    }
}
