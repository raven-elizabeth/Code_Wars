namespace CodeWars;

public class RemoveMin
{
    public static List<int> RemoveSmallest(List<int> numbers)
    {
        return (numbers.Count > 1) ? new List<int>(numbers.Where((i, idx) => idx != numbers.IndexOf(numbers.Min()))) : new List<int>();

    }
}