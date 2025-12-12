namespace CodeWars;

public class SumOfFirstNthTermOfSeries
{
    public static string seriesSum(int n)
    {
        if (n == 0)
        {
            return "0.00";
        }

        decimal sum = 0m;
        for (int i = 1; i < n * 3; i += 3)
        {
            sum += 1m / i;
        }
        return $"{Math.Round(sum, 2)}";
    }
}
