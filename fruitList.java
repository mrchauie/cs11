import java.util.LinkedList;
import Classes.Fruit;
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.PrintWriter;
import java.io.FileWriter;

public class fruitList {
    //reads fruits from a file and puts them into a list

    public static void main(String[] args) {
        LinkedList<Fruit> list = new LinkedList<Fruit>();
        String fruit = "";
        //read a file with fruits
        try {
            FileReader fr = new FileReader("./cs11/fruits.txt");
            BufferedReader reader = new BufferedReader(fr);   

            while ((fruit = reader.readLine()) != null) {
                System.out.println(fruit);
                Fruit f = new Fruit(fruit);
                list.add(f);
            }
            reader.close();
        } catch (IOException e) {
            System.out.println("OOPS! Error reading!");
            System.out.println(e);
        }

        //create a new fruit and add it to the fruitsList
        list.add(new Fruit("strawberry"));

        //read a file with fruits
        try {
            FileWriter fw = new FileWriter("./cs11/fruits.txt");
            PrintWriter writer = new PrintWriter(fw);
            for (int i = 0; i < list.size(); i++) {
                writer.println(list.get(i).name);
            }
            
            writer.close();
        } catch (IOException e) {
            System.out.println("OOPS! Error writing!");
        }
    }
}
