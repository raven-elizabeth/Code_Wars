namespace CodeWars;
public class GetMiddleChar
{
    public static string GetMiddle(string s)
    {
        int mid = s.Length / 2;
        return (s.Length % 2 == 0) ? $"{s[mid - 1]}{s[mid]}" : $"{s[mid]}";
    }
}
