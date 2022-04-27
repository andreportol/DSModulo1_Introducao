import java.util.Scanner;

public class Par_Impar {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        System.out.print("Quantos numeros vc vai digitar:");
        int quantidade = Integer.parseInt(s.next());
        for (int i = 0; i < quantidade; i++) {
            String par_impar = "";
            String maior_menor = "";
            System.out.print("Digite um numero: ");
            int n = Integer.parseInt(s.next());
            if (n % 2 == 0 && n != 0) {
                par_impar = "PAR";
            } else if (n != 0){
                par_impar = "IMPAR";
            }
            if (n > 0) {
                maior_menor = "POSITIVO";
            }else if(n < 0){
                maior_menor = "NEGATIVO";
            }else{
               System.out.print("NULO"); 
            }
            System.out.println(par_impar + "  " +maior_menor);
        }

        s.close();
    }
}
