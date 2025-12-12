namespace CodeWars;

public class FindFirstNonConsecutiveNum
{
    public static object FirstNonConsecutive(int[] arr)
    {
        int last = arr[0];
        for (int i = 1; i < arr.Length; i++)
        {
            if (arr[i] != last + 1)
            {
                return arr[i];
            }
            last = arr[i];
        }
        return null;
    }
}
