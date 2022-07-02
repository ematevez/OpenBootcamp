/*Enunciado del ejercicio:
Para practicar la encapsulación:
Crear clase Persona.
Crear variables las privadas edad, nombre y telefono de la clase Persona.
Crear gets y sets de cada propiedad.
Crear un objeto persona en el main.

Utiliza los gets y sets para darle valores a las propiedades edad, nombre y telefono,
por último muéstralas por consola.
*/
import java.util.ArrayList;

public class Main {

    public static void main(String[] args) {
        Persona Jose = new Persona();
        Jose.setEdad(35);
        Jose.setNombre("JOSE");
        Jose.setTelefono(123123);

        System.out.println("NOMBRE: " + Jose.getNombre() + "\nEDAD: " + Jose.getEdad() + "\nTELEFONO: " + Jose.getTelefono());
    }
}
class Persona{
        private int edad;
        private String nombre;
        private int telefono;

        public void setEdad(int edad){
            this.edad=edad;
        }
        public int getEdad(){
            return this.edad;
        }

        public void setNombre(String nombre){
            this.nombre=nombre;
        }

        public String getNombre(){
            return this.nombre;
        }

        public void setTelefono(int telefono){
            this.telefono=telefono;
        }

        public int getTelefono(){
            return this.telefono;
        }
 }
