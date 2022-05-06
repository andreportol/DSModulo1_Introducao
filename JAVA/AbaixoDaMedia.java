import java.util.Scanner;

public class AbaixoDaMedia {
    public static void main(String[] args) {
        // variáveis
        int quantidade;
        double numero, media = 0;
        // criando vetor
        Scanner s = new Scanner(System.in);
        System.out.println("Quantos elementos vai ter o vetor: ");
        quantidade = s.nextInt();
        double[] vetor = new double[quantidade];
        double[] menorMedia = new double[quantidade];
        // inserindo valores no vetor
        for (int i = 0; i < quantidade; i++) {
            System.out.print("Digite um número: ");
            numero = s.nextDouble();
            vetor[i] = numero;
        }
        // calculando a média dos valores
        for (int i = 0; i < quantidade; i++) {
            media += vetor[i];
        }
        // exibindo média
        double media_final = media / vetor.length;
        System.out.printf("Media dos valores = %.1f\n", media_final);
        // comparando valores e exibindo
        System.out.print("Valores abaixo da média = ");
        for (int i = 0; i < quantidade; i++) {
            if (vetor[i] < media_final) {
                menorMedia[i] = vetor[i];
                System.out.print(menorMedia[i] + " ");
            }

        }
        s.close();
    }
}
