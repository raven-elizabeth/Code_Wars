namespace CodeWars;

public class MovingZeroesToEnd
{
    public static int[] MoveZeroes(int[] arr)
    {
        int[] zeroesMoved = new int[arr.Length];
        int idx = 0;

        foreach (int i in arr)
        {
            if (i != 0)
            {
                zeroesMoved[idx] = i;
                idx++;
            }
        }
        return zeroesMoved;
    }
}
