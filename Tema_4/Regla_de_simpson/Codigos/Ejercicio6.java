// Java program to evaluate the given expression
import java.util.*;
 
class gfg
{
// Function to find the sum
public static double calculateSum(double n)
{
    return 2 * (Math.pow(n, 6) + 15 * Math.pow(n, 4) 
            + 15 * Math.pow(n, 2) + 1);
}
 
// Driver Code
public static void main(String[] args)
{
    double n = 1.4142;
    System.out.println((int)Math.ceil(calculateSum(n)));
}
}
//This code is contributed by mits
