class Fruit {
    //attributes
    String name;

    //constructor for parent/super class
    public Fruit(String n) {
        name = n;  
        System.out.println("Created a new Fruit!");
    }
    
    public void wash() {
        System.out.println("Washing the fruit...");
    }

    //overloading the wash method
    public void wash(String person) {
        System.out.println(person + " is washing the fruit.");
    }
}

class Apple extends Fruit {
    //new attributes
    String colour;

    //constructor for child/subclass
    public Apple(String n, String c) {
        super(n); //initialise the child with the parent attributes
        colour = c;
        System.out.println("Created a new Apple!");
    }

    //example of polymorphic method
    public void wash() {
        System.out.println("Washing the apple...");
    }
}

class Orange extends Fruit {
    String colour;
    //constructor for child/subclass
    public Orange(String n, String c) {
        super(n); //initialise the child with the parent attributes
        colour = c;
        System.out.println("Created a new Orange!");
    }

    public void wash() {
        System.out.println("Washing the orange...");
    }
}

public class Main {
    public static final void main(String[] args) {
        Fruit f = new Fruit("apple"); //instantiate Fruits object
        f.wash();

        Apple a = new Apple("Gala", "red"); //instantiate Apple object
        a.wash();

        Orange o = new Orange("Sunkist", "orange"); //instantiate Orange object
        o.wash();
        o.wash("Mike");
    }
}