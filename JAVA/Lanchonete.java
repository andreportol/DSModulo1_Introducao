import java.util.Scanner;

public class Lanchonete {

    public double calcularValor(int codigo, int quantidade) {
        if (codigo == 1) {
            double valor = quantidade * 5;
            return valor;
        } else if (codigo == 2) {
            double valor = quantidade * 3.5;
            return valor;
        } else if (codigo == 3) {
            double valor = quantidade * 4.8;
            return valor;
        } else if (codigo == 4) {
            double valor = quantidade * 8.9;
            return valor;
        } else if (codigo == 5) {
            double valor = quantidade * 7.32;
            return valor;
        }
        return 0;
    }

    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        System.out.println("Codigo do produto comprado: ");
        int codigo = Integer.parseInt(s.next());
        System.out.println("Quantidade comprada: ");
        int quantidade = Integer.parseInt(s.next());
        Lanchonete lan1 = new Lanchonete();
        // formatando valor para duas casas decimais
        String resultado = String.format("%.2f", lan1.calcularValor(codigo, quantidade));
        System.out.println("Valor a pagar: " + resultado);

        s.close();
    }
}