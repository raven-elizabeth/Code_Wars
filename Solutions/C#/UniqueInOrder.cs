namespace CodeWars;

public class UniqueInOrder
{
    public static IEnumerable<T> UniqueOrder<T>(IEnumerable<T> iterable)
    {
        // Assign first previous value as default of object type
        T prevValue = default(T);

        // Foreach loop through each object in iterable
        foreach (T val in iterable)
        {

            // If current value is not the same as previous value, yield return this value
            if (!val.Equals(prevValue))
            {
                prevValue = val;
                yield return val;
            }
        }
    }
}
