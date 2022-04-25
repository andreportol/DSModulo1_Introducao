import java.util.Scanner;

public class Lanchonete_Version1 {
    public static double[] valor = {5.00,3.50,4.80,8.90,7.32};
    
    public double calcularValor(int indice,int quantidade){
        indice -= 1;
        double total = Lanchonete_Version1.valor[indice] * quantidade;
        return total;
    }
    public static void main(String []args) {
        Scanner s = new Scanner(System.in);
        Lanchonete_Version1 lan1 = new Lanchonete_Version1();
        
        System.out.println("Codigo do produto comprado: ");
        int indice = Integer.parseInt(s.next());
        System.out.println("Quantidade comprada: ");
        int quantidade = Integer.parseInt(s.next());
        String resultado = String.format("%.2f",lan1.calcularValor(indice, quantidade));
        System.out.println("Valor a pagar: "+resultado);
        s.close();
    }
}
