import java.util.Scanner;

public class Matriz_Geral {

    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        // variáveis
        int ordem = 0, indice = 0, coluna = 0;
        double elemento = 0;
        double somatorio = 0;

        // matriz
        System.out.print("Qual a ordem da matriz? ");
        ordem = s.nextInt();
        double[][] matriz = new double[ordem][ordem];
        // inserindo elementos na matriz
        for (int l = 0; l < ordem; l++) {
            for (int c = 0; c < ordem; c++) {
                System.out.printf("Elemento [%d %d]: ", l, c);
                elemento = s.nextDouble();
                matriz[l][c] = elemento;
            }
        }

        // calculando a soma de todos os elementos positivos da matriz
        for (int l = 0; l < ordem; l++) {
            for (int c = 0; c < ordem; c++) {
                if (matriz[l][c] > 0) {
                    somatorio += matriz[l][c];
                }
            }
        }
        System.out.println("Somatorio: " + somatorio);

        // ler o indice de uma linha e imprimir todos os elementos dessa linha
        System.out.print("Escolha uma linha: ");
        indice = s.nextInt();
        System.out.print("LINHA ESCOLHIDA: ");
        for (int l = 0; l < ordem; l++) {
            for (int c = 0; c < ordem; c++) {
                if (l == indice) {
                    System.out.print(" " + matriz[l][c]);
                }
            }
        }
        System.out.println("");
        // ler o indice de uma coluna e imprimir todos os elementos dessa coluna
        System.out.print("Escolha uma coluna: ");
        indice = s.nextInt();
        System.out.print("COLUNA ESCOLHIDA: ");
        for (int l = 0; l < ordem; l++) {
            for (int c = 0; c < ordem; c++) {
                if (c == indice) {
                    System.out.print(" " + matriz[l][c]);
                }
            }
        }
        System.out.println("");
        // imprimir os elementos da diagonal principal
        System.out.print("DIAGONAL PRINCIPAL: ");
        for (int l = 0; l < ordem; l++) {
            for (int c = 0; c < ordem; c++) {
                if (l == c) {
                    System.out.print(matriz[l][c] + " ");
                }
            }

        }
        System.out.println("");

        // elevar todos os números negativos ao quadrado
        System.out.println("MATRIZ ALTERADA: ");
        for (int l = 0; l < ordem; l++) {
            for (int c = 0; c < ordem; c++) {
                if (matriz[l][c] < 0) {
                    elemento = matriz[l][c];
                    elemento = elemento * elemento;
                    matriz[l][c] = elemento;
                }
                System.out.printf(matriz[l][c] + " ");
            }
            System.out.println("");
        }
        s.close();
    }
}
