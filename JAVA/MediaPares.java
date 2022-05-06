import java.util.Scanner;

public class MediaPares {
    public static void main(String[] args) {
        // variáveis
        int contadorPar = 0, numero = 0;
        double media_aritmetica = 0;

        // criando vetores
        Scanner s = new Scanner(System.in);
        System.out.println("Quantos elementos vai ter o vetor? ");
        int quantidade = s.nextInt();
        int[] vetorA = new int[quantidade];
        // inserindo valores no vetor A
        for (int i = 0; i < quantidade; i++) {
            System.out.print("Digite um número: ");
            numero = s.nextInt();
            vetorA[i] = numero;
        }
        // verificando os elementos pares do vetor A
        for (int i = 0; i < quantidade; i++) {
            if (vetorA[i] % 2 == 0) {
                media_aritmetica += vetorA[i];
                contadorPar += 1;
            }
        }
        double media_aritmetica1 = media_aritmetica / contadorPar;
        if (contadorPar != 0) {
            System.out.printf("Média aritmética dos números pares = %.1f", media_aritmetica1);
        } else
            System.out.println("NENHUM NUMERO PAR");
        s.close();
    }
}
