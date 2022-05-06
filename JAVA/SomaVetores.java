import java.util.Scanner;

public class SomaVetores {
    public static void main(String[] args) {
        // variáveis
        double numero;
        // criando vetores
        Scanner s = new Scanner(System.in);
        System.out.println("Quantos valores vão ter cada vetor? ");
        int quantidade = s.nextInt();
        double[] vetorA = new double[quantidade];
        double[] vetorB = new double[quantidade];
        double[] vetorC = new double[quantidade];
        // inserindo valores no vetor A
        System.out.println("Digite os valores do vetor A: ");
        for (int i = 0; i < quantidade; i++) {
            numero = s.nextDouble();
            vetorA[i] = numero;
        }
        // inserindo valores no vetor B
        System.out.println("Digite os valores do vetor B: ");
        for (int i = 0; i < quantidade; i++) {
            numero = s.nextDouble();
            vetorB[i] = numero;
        }
        // somando valores dos vetores
        for (int i = 0; i < quantidade; i++) {
            vetorC[i] = vetorA[i] + vetorB[i];
        }
        // imprimindo vetorC
        System.out.print("vetor C = [ ");
        for (int i = 0; i < quantidade; i++) {
            System.out.print(vetorC[i] + " ");
        }
        System.out.println("]");
        s.close();

    }

}
