import java.util.Scanner;

public class ParesConsecutivos {
    public static void main(String[] args) {
        boolean loop = true;
        int valor_soma = 0;
        int[] soma = new int[5];
        Scanner s = new Scanner(System.in);
        while (loop) {
            valor_soma = 0;
            System.out.println("Digite um numero inteiro: ");
            int valor_digitado = Integer.parseInt(s.next());
            if (valor_digitado == 0) {
                System.out.println("Exit");
                break;
            } else {
                if (valor_digitado % 2 == 0) {
                    for (int x = 0; x < 5; x++) {
                        soma[x] = valor_digitado;
                        valor_digitado += 2;
                        valor_soma += soma[x];
                    }
                    System.out.println("Soma: " + valor_soma);
                } else {
                    valor_digitado += 1;
                    for (int x = 0; x < 5; x++) {
                        soma[x] = valor_digitado;
                        valor_digitado += 2;
                        valor_soma += soma[x];
                    }
                    System.out.println("Soma: " + valor_soma);
                }
            }
        }
        s.close();
    }
}
