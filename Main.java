class Fruit {
    //attributes
    String name;

    //constructor for parent/super class
    public Fruit(String n) {
        name = n;  
    }
}

class Apple extends Fruit {
    //new attributes
    String colour;

    //constructor for child/subclass
    public Apple(String n, String c) {
        super(n); //initialise the child with the parent attributes
        colour = c;
    }
}

public class Main {
    public static final void main(String[] args) {
        Fruit f = new Fruit("apple"); //instantiate Fruits object
        System.out.println(f.name); //print the fruit's name

        Apple a = new Apple("Gala", "red"); //instantiate Apple object
        System.out.println(a.name + " " + a.colour); //print the name and colour of the apple
    }
}