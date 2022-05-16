import java.util.Scanner;

public class Acima_Diagonal {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        // variáveis
        int elemento = 0;
        int somatorio = 0;
        // matriz
        System.out.print("Qual a ordem da matriz? ");
        int ordem = s.nextInt();
        int[][] matriz = new int[ordem][ordem];

        // inserindo elementos na matriz
        for (int l = 0; l < ordem; l++) {
            for (int c = 0; c < ordem; c++) {
                System.out.printf("Elemento [%d, %d]: ", l, c);
                elemento = s.nextInt();
                matriz[l][c] = elemento;
            }
        }
        // calcular somatorio dos elementos acima da diagonal principal
        for (int l = 0; l < ordem; l++) {
            for (int c = 0; c < ordem; c++) {
                if(c>l){
                    elemento = matriz[l][c];
                    somatorio += elemento;
                }
            }
        }
        System.out.println("SOMA DOS ELEMENTOS ACIMA DA DIAGONAL PRINCIPAL: "+ somatorio);
        s.close();
    }

}