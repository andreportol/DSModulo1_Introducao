import java.util.Arrays;
import java.util.Scanner;

public class MaiorPosicao {
    public static void main(String[] args) {
        // variáveis
        int quantidade;
        double numero;
        double maior_valor = 0;
        int indiceMaiorValor = 0;
        // criando vetor de numeros
        Scanner s = new Scanner(System.in);
        System.out.println("Quantos números vc vai digitar: ");
        quantidade = s.nextInt();
        double[] vetor = new double[quantidade];
        // inserindo dados no vetor
        for (int i = 0; i < quantidade; i++) {
            System.out.print("Digite um número: ");
            numero = s.nextDouble();
            vetor[i] = numero;
        }
        // Maior valor
        for (int i = 0; i < quantidade; i++) {
            if (vetor[i] > maior_valor) {
                maior_valor = vetor[i];
                indiceMaiorValor = i;
            }
        }
        System.out.printf("Maior valor = %.2f\n", maior_valor);
        System.out.printf("Posição do maior valor = %d", indiceMaiorValor);
        s.close();
    }
}
