namespace CodeWars;

public class MoneyMoneyMoney
{
    public static int CalculateYears(double principal, double interest, double tax, double desiredPrincipal)
    {
        int years = 0;
        while (principal < desiredPrincipal)
        {
            principal += (principal * interest) * (1 - tax);
            years++;
        }
        return years;
    }
}
