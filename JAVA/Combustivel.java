import java.util.Scanner;

public class Combustivel {
    int alcool, gasolina, diesel;

    public void contarTipoCombustivel(int tipo) {
        if (tipo == 1) {
            alcool += 1;
        } else if (tipo == 2) {
            gasolina += 1;
        } else if (tipo == 3) {
            diesel += 1;
        }
    }

    public boolean validarCodigo(int codigo) {
        if (codigo <= 0 || codigo >= 4) {
            return false;
        } else {
            return true;
        }
    }

    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        Combustivel c = new Combustivel();
        boolean sair = true;
        while (sair) {
            System.out.print("Informe um codigo (1, 2, 3) ou 4 para parar: ");
            int codigo = Integer.parseInt(s.next());
            boolean valor = c.validarCodigo(codigo);
            if (valor) {
                c.contarTipoCombustivel(codigo);
            } 
            else if (codigo == 4) {
                System.out.println("MUITO OBRIGADO");
                break;
            }
        }
        System.out.println("Alcool: " + c.alcool);
        System.out.println("Gasolina: " + c.gasolina);
        System.out.println("Diesel: " + c.diesel);
        s.close();
    }
}
