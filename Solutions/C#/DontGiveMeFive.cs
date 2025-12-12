namespace CodeWars;

public class DontGiveMeFive
{
    public static int DontGiveMe5(int start, int end)
    {
        return Enumerable.Range(start, end - start + 1).Where(i => !i.ToString().Contains("5")).Count();
    }
}
