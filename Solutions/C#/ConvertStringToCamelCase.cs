using System.Globalization;

namespace CodeWars;

public class ConvertStringToCamelCase
{
    public static string ToCamelCase(string str)
    {
        TextInfo ti = new CultureInfo("en-GB").TextInfo;
        return (str.Length < 2) ? str : str[0] + ti.ToTitleCase(str).Substring(1).Replace("-", "").Replace("_", "");
    }
}
