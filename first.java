class first {
    public static void main(String[] args) {
        int j = 0;
        char c = 'C';
        String s = "hello world!";
        int[] a = new int[10]; //list example
        double d = 20.0; 

        // print characters and strings
        System.out.println("This is a " + c);
        System.out.println(s);
        System.out.println(d + 50);

        // for loop
        for (int i = 0; i < 10; i++) {
            System.out.println(i);
        }

        // while loop
        while (j < 10) {
            if (j < 5) {
                System.out.println(j);
            }
            j = j + 1;
        }

        // arrays
        for (int i = 0; i < 10; i++) {
            a[i] = i;
            System.out.println(a[i]);
        }
    }
}

