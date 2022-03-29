import java.util.Scanner;

public class EncargadoEficiente {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        System.out.println("¿Cuántos libros quieres agregar?");
        String cantidad = sc.nextLine();
        int cantidadT = Integer.parseInt(cantidad);

        String[] libros = new String[cantidadT];
        String[] disponibilidad = new String[cantidadT];

        for(int i = 0; i < cantidadT; i++){
            System.out.println("Ingresa el título del libro " + (i+1));
            String titulo = sc.nextLine();
            libros[i] = titulo;
            System.out.println("Ingresa su disponibilidad");
            String disponible = sc.nextLine();
            disponibilidad[i] = disponible;
        }

        System.out.println("¿Cuál libro quieres consultar?");
        String requerido = sc.nextLine();
        for(int i = 0; i < libros.length; i ++){
            if(requerido.equals(libros[i])){
                System.out.println("La disponibilidad de " + requerido + " es: " + disponibilidad[i]);
            }
        } 
    }
}
