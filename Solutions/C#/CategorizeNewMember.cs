namespace CodeWars;

public class CategorizeNewMember
{
    public static IEnumerable<string> OpenOrSenior(int[][] data)
    {
        return data.Select(memberDetails => (memberDetails[0] >= 55 && memberDetails[1] > 7) ? "Senior" : "Open");
    }
}
