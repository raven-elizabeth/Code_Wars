namespace CodeWars;

public class DoesMyNumLookBig
{
    public static bool Narcissistic(int value)
    {
        string val = value.ToString();

        int total = 0;
        foreach (char i in val)
        {
            total += (int)Math.Pow(i - 48, val.Length);
        }

        return total == value;
    }
}
