import java.util.Scanner;
import java.util.Arrays;

public class Mediana{
  
/**
 * Método para obtener la mediana de un arreglo ordenado y suponiendo que tiene longitud impar
 * @param arreglo el arreglo del que se obtiene la mediana
 * @return la mediana del arreglo
 */
public static int regresaMediana(int[] arreglo){
    return arreglo[arreglo.length/2];
}

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        System.out.println("Introduce la longitud del arreglo");
        int size = sc.nextInt();
        int[] arreglo = new int[size];
        
        for(int i = 0; i < size; i++){
            System.out.println("Introduce el elemento en la posición " + i + ":");
            arreglo[i] = sc.nextInt();
        }

        System.out.println("\n");

        Arrays.sort(arreglo);
        System.out.println("**************");
        System.out.println("La mediana es: " + regresaMediana(arreglo));
        System.out.println("Su índice es: " + arreglo.length/2);
    }
}