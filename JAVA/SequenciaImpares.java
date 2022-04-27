import java.util.Scanner;

public class SequenciaImpares {
    public static void main(String[]args) {
        Scanner s = new Scanner(System.in);
        System.out.print("Digite o valor de X: ");
        int x = Integer.parseInt(s.next());
        for(int i = 1; i <=x; i+=2){
            System.out.println(i);
        }
        s.close();
    }
}
