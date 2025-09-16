package Solutions.Java;

// There was a test in your class and you passed it. Congratulations!
// But you're an ambitious person. You want to know if you're better than the average student in your class.
// You receive an array with your peers' test scores. Now calculate the average and compare your score!
// Return true if you're better, else false!
// Note:Your points are not included in the array of your class's points. Do not forget them when calculating the average score!

// My initial solution:
// public class BetterThanAverage {
//     public static boolean betterThanAverage(int[] classPoints, int yourPoints) {
        
//         int sum = yourPoints;
//         for(int i = 0; i < classPoints.length; i++) {
//             sum += classPoints[i];
//         }
    
//     int avg = sum / (classPoints.length + 1);
    
//     return (yourPoints > avg) ? true:false;
//     }
// }

// My refactored solution:
public class BetterThanAverage {
    public static boolean betterThanAverage(int[] classPoints, int yourPoints) {
    
        int sum = yourPoints;
        for(int i : classPoints) {
        sum += i;
        }
    
        int avg = sum / (classPoints.length + 1);
    
        return (yourPoints > avg) ? true:false;
    }
}

// Alternative with utils
// import java.util.Arrays;

// public class BetterThanAverage {
//     static boolean betterThanAverage(final int[] classPoints, final int yourPoints) {
//         return Arrays.stream(classPoints).average().orElse(0) < yourPoints;
//     }
// }