import java.util.Scanner;

public class MaisVelho {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        // variáveis
        int quantidade = 0;
        String nome;
        int idade;
        // criando os vetores
        System.out.print("Quantas pessoas vc vai digitar: ");
        quantidade = s.nextInt();
        String[] nomes = new String[quantidade];
        int[] idades = new int[quantidade];
        // inserindo valores nos vetores nomes e idades
        for (int i = 0; i < quantidade; i++) {
            System.out.printf("Dados da %dº pessoa:\n", i + 1);
            System.out.print("Nome: ");
            nome = s.next();
            nomes[i] = nome;
            System.out.print("Idade: ");
            idade = s.nextInt();
            idades[i] = idade;
        }
        // Calculando e exibindo a pessoa mais velha
        int maiorIdade = idades[0];
        int indice = 0;
        for (int i = 1; i < quantidade; i++) {
            if (idades[i] > maiorIdade) {
                maiorIdade = idades[i];
                indice = i;
            }
        }
        System.out.print("Nome da pessoa mais velha: " + nomes[indice]);
        System.out.println(". Sua idade é: " + idades[indice] + " anos.");
        s.close();
    }
}
