package devsuperior;

import java.util.Scanner;

public class Comerciante {

	public static void main(String[] args) {
		Scanner s = new Scanner(System.in);
		// variáveis
		int quantidade = 0;
		String nome;
		int cont_lucro_10 = 0, cont_lucro_10_20 = 0, cont_lucro_20 = 0;
		double precoCompra, precoVenda, lucro = 0;
		double totalCompra =0, totalVenda = 0, totalLucro = 0;
		// criando os arrays
		System.out.print("Serão digitados dados de quantos produtos: ");
		quantidade = s.nextInt();
		String[] nomes = new String[quantidade];
		double[] precoCompras = new double[quantidade];
		double[] precoVendas = new double[quantidade];
		// inserindo dados nos arrays
		for (int i = 0; i < quantidade; i++) {
			System.out.printf("Produto %d: \n", i + 1);
			System.out.print("Nome: ");
			nome = s.next();
			System.out.print("Preço de compra: ");
			precoCompra = s.nextDouble();
			System.out.print("Preço de venda: ");
			precoVenda = s.nextDouble();
			nomes[i] = nome;
			precoCompras[i] = precoCompra;
			precoVendas[i] = precoVenda;
		}
		// calculando 
		for (int i = 0; i < quantidade; i++) {
			lucro = ((precoVendas[i] / precoCompras[i]) - 1) * 100;
			System.out.println(lucro);
			if (lucro < 10) {
				cont_lucro_10 += 1;
			} else if (lucro >= 10 && lucro <= 20) {
				cont_lucro_10_20 += 1;
			} else if (lucro > 20) {
				cont_lucro_20 += 1;
			}
		}
		for (int i = 0; i < quantidade; i++) {
			totalCompra += precoCompras[i];
			totalVenda += precoVendas[i];
		}
		totalLucro = totalVenda - totalCompra;
		// exibindo os dados
		System.out.println("RELATÓRIO: ");
		System.out.printf("Lucro abaixo de 10 porcento: %d\n", cont_lucro_10);
		System.out.printf("Lucro entre 10 e 20 porcento: %d\n", cont_lucro_10_20);
		System.out.printf("Lucro acima de 20 porcento: %d\n", cont_lucro_20);
		System.out.printf("Valor de total de compra: %.2f\n", totalCompra);
		System.out.printf("Valor de total de venda: %.2f\n", totalVenda);
		System.out.printf("Lucro total: %.2f\n", totalLucro);
		
		s.close();
	}

}
