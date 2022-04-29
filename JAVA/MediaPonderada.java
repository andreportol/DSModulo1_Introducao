import java.util.Scanner;

public class MediaPonderada {
    public static void main(String[] args){
        Scanner s = new Scanner(System.in);
        System.out.println("Quantos casos vc vai digitar?");
        int num_casos = Integer.parseInt(s.next());
        for(int i=0; i < num_casos;i++){
            System.out.println("digite três numeros: ");
            double num1 = Double.parseDouble(s.next());
            double num2 = Double.parseDouble(s.next());
            double num3 = Double.parseDouble(s.next());
            double media = (num1*2 + num2*3+num3*5)/10;
            System.out.printf("Media= %.1f%n", media);
        }
        
        
        
        s.close();
    }
}
