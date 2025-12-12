namespace CodeWars;

public class FindDivisors
{
    public static int[] Divisors(int n)
    {
        List<int> d = new List<int>();
        // Halve, start from 2
        for (int i = 2; i <= n / 2; i++)
        {
            if (n % i == 0)
            {
                //add i to arr
                d.Add(i);
            }
        }
        // return null if arr is empty, else arr
        return (d.ToArray().Length > 0) ? d.ToArray() : null;
    }
}
