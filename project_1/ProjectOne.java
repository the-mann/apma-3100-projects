import java.math.BigInteger;
import java.util.ArrayList;
import java.util.List;

public class ProjectOne {

    public static void main(String[] args) {

        // Problem 1
        // Write a program using for loops that lists AND counts all the possible book orders.
        // What are the first 20 outcomes that your program lists? What is the total number
        // of outcomes?
        List<String> classes = new ArrayList<>();
        classes.add("astronomy");
        classes.add("calculus");
        classes.add("French");
        classes.add("history");
        classes.add("literature");
        classes.add("organic chemistry");
        classes.add("physics");

        int orders = 0;
        for (int i=1; i<=classes.size(); i++) {
            for (int j=1; j<=classes.size(); j++) {
                if (i == j) {
                    break;
                }
                for (int k=1; k<=classes.size(); k++) {
                    if ((i == k) || (j == k)) {
                        break;
                    }
                    for (int l=1; l<=classes.size(); l++) {
                        if ((l == i) || (l == j) || (l==k)) {
                            break;
                        }
                        orders++;
                        // outputs the first 20 book orders in alphabetical order
                        if (orders <= 20) {
                            System.out.println(classes.get(l - 1) + ", " + classes.get(k - 1) + ", " + classes.get(j - 1) + ", " + classes.get(i - 1));
                        }
                    }
                }
            }
        }

        System.out.println("Total orders: " + orders);

        // Problem 2
        // An 8-digit password is required to have three 0’s and five 1’s. You will determine how many unique
        // passwords are possible.
        // Note: using the positions of the 0's as the passcodes
        int counter = 0;
        System.out.print("{ ");
        for (int i=1; i<=8; i++) {
            for (int j=1; j<=8; j++) {
                if (j == i) {
                    break;
                }
                for (int k=1; k<=8; k++) {
                    if (k == i || k == j) {
                        break;
                    }
                    System.out.print("(" + k + "" + j + "" + i + ") ");
                    counter++;
                    if (counter %10 == 0) {
                        System.out.println();
                    }
                }
            }
        }
          System.out.println("}");
        System.out.println("Total passwords: " + counter);

        // Problem 2, part B
        // Now suppose a 30-digit password is required to have thirteen 0’s and seventeen 1’s.
        // You don’t need to list all the possible passwords, but you need to determine how many exist.
        int length = 30;
        int zeroes = 13;
        System.out.println("Total passwords: " + passwords(length, zeroes));

    }

    public static BigInteger passwords(int length, int zeroes) {
        // n!/(k!*(n-k)!)
        BigInteger numerator = BigInteger.valueOf(length);
        for (int i=length-1; i > (length-zeroes); i-- ) {
            numerator = numerator.multiply(BigInteger.valueOf(i));
        }

        BigInteger denominator = BigInteger.valueOf(zeroes);
        for (int i=zeroes-1; i>0; i--) {
            denominator = denominator.multiply(BigInteger.valueOf(i));
        }

        return numerator.divide(denominator);
    }
}


