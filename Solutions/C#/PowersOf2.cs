using System.Numerics;

namespace CodeWars;

public class PowersOf2
{
    public static BigInteger[] PowersOfTwo(int n)
    {
        BigInteger[] arr = new BigInteger[n + 1];

        for (int i = 0; i <= n; i++)
        {
            arr[i] = (BigInteger)Math.Pow(2, i);
        }

        return arr;
    }
}
