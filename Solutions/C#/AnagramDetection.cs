namespace CodeWars;

public class AnagramDetection
{
    public static bool IsAnagram(string a, string b)
    {
        a = a.ToLower();
        b = b.ToLower();

        foreach (char c in a)
        {
            if (b.Contains(c))
            {
                b = b.Remove(b.IndexOf(c), 1);
                a = a.Remove(a.IndexOf(c), 1);
            }
        }
        return b.Length == 0 && a.Length == 0;
    }
}
