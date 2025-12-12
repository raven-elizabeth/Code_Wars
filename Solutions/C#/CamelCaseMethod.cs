using System.Globalization;

namespace CodeWars;

public static class CamelCaseMethod
{
    public static string CamelCase(this string str)
    {
        return new CultureInfo("en-GB").TextInfo.ToTitleCase(str).Replace(" ", "");
    }
}
