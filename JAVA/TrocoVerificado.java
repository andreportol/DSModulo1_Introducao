import java.util.Scanner;

public class TrocoVerificado {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        System.out.println("Preco unitario do produto: ");
        double preco = Double.parseDouble(s.next());
        System.out.println("Quantidade comprada: ");
        int quantidade = Integer.parseInt(s.next());
        System.out.println("Dinheiro recebido: ");
        double dinheiro_recebido = Double.parseDouble(s.next());
        if (preco * quantidade <= dinheiro_recebido) {
            System.out.println("Troco: " + (dinheiro_recebido - (preco * quantidade)));
        } else
            System.out.println("Dinheiro insuficiente. Faltam " + (preco * quantidade - dinheiro_recebido) + " reais.");

        s.close();
    }

}
