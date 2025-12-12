namespace CodeWars;

public class ShortestWord
{
    public static int FindShort(string s)
    {
        return s.Split(" ").Min(word => word.Length);
    }
}
