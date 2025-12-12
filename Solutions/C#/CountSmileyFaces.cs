using System.Text.RegularExpressions;

namespace CodeWars;

public static class CountSmileyFaces
{
    public static int CountSmileys(string[] smileys)
    {
        return smileys.Count(face => Regex.IsMatch(face, @"[:;][-~]?[)D]"));
    }
}
