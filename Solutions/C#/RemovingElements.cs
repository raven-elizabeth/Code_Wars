namespace CodeWars;

public class RemovingElements
{
    public static object[] RemoveEveryOther(object[] arr)
    {
        return arr.Where((i, idx) => idx % 2 == 0).ToArray();
    }
}
