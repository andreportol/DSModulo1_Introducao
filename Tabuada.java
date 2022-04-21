import java.util.Scanner;

public class Tabuada {
    public static void exibirTabuada(int valor){
        for(int i = 1; i < 11; i++){
            System.out.println(valor+" * "+ i +" = " + (i*valor));
        }
    }
    public static void main(String[]args){
        Scanner s = new Scanner(System.in);
        System.out.println("Deseja a tabuada para qual valor: ");
        int numero = Integer.parseInt(s.next());
        Tabuada.exibirTabuada(numero);
        
        s.close();
    }
}
