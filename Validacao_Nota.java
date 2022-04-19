import java.util.Scanner;

public class Validacao_Nota{
    float nota1, nota2;
    static boolean loop = true;
    
    public boolean validarNota1(float nota1){
        if(nota1 >= 0 && nota1 <= 10){
            return true;
        }
        else{
            return false;
        }
    }
    public boolean validarNota2(float nota2){
        if(nota2 >= 0 && nota2 <= 10){
            return true;
        }
        else{
            return false;
        }
    }
   
    public static void main(String[]args){
        Validacao_Nota vn = new Validacao_Nota();
        Scanner s = new Scanner(System.in);
        System.out.println("Digite a primeira nota: ");
        vn.nota1 = Float.parseFloat(s.next()); 
        while(loop){
            if(vn.validarNota1(vn.nota1)){
                System.out.println("Digite a segunda nota: ");
                vn.nota2 = Float.parseFloat(s.next());
                if(vn.validarNota2(vn.nota2)){
                    float media = (vn.nota1 + vn.nota2)/2;
                    System.out.println("Media final:"+ media);
                    break;
                }
                else{
                    while(loop){
                        System.out.println("Valor invalido! Digite novamente: ");
                        vn.nota2 = Float.parseFloat(s.next());
                        if(vn.validarNota2(vn.nota2)){
                            float media = (vn.nota1 + vn.nota2)/2;
                            System.out.println("Media final:"+ media);
                            loop = false;
                            break;
                        }
                    }
                }
            }else{
                System.out.println("Valor invalido! Digite novamente: ");
                vn.nota1 = Float.parseFloat(s.next());
            } 
        }
        s.close(); 
    }
        
        
         
         
        

}

   