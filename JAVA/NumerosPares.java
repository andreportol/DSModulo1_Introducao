import java.util.Scanner;

public class NumerosPares{
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        System.out.println("Quantos numeros vc vai digitar:");
        int quantidade = s.nextInt();
        int[] vetor = new int[quantidade];
        // inserindo dados no vetor 
        for(int i=0; i<quantidade;i++){
            System.out.print("Digite um numero: ");
            int numero = s.nextInt();
            vetor[i] = numero;
        }
        // exibindo os dados e contando os numeros pares
        System.out.println("Números pares: ");
        int contador = 0;
        for(int i=0; i<quantidade;i++){
            int numero_par = vetor[i];
                if(numero_par % 2 == 0){
                System.out.print(numero_par + " ");
                contador += 1;
            }
        }
        System.out.println();
        System.out.println("QUANTIDADE DE PARES = " + contador);
        s.close();
    }
}