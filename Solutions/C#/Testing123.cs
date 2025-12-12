namespace CodeWars;

public class Testing123
{
    public static List<string> Number(List<string> lines)
    {
        return (lines.Any()) ? lines.Select((i, idx) => $"{idx + 1}: {i}").ToList() : lines;
    }
}
