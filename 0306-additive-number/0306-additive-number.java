import java.math.BigInteger;
import java.util.Arrays;
import java.util.List;

class Solution {
    public boolean isAdditiveNumber(String num) {
        int n = num.length();
        // First number ends at i-1, second number ends at j-1
        for (int i = 1; i <= n - 2; i++) {
            // leading zero check for first number
            if (num.charAt(0) == '0' && i > 1) break;

            for (int j = i + 1; j <= n - 1; j++) {
                // leading zero check for second number
                if (num.charAt(i) == '0' && j - i > 1) break;

                if (isValid(num, 0, i, j)) return true;
            }
        }
        return false;
    }

    // num[aStart..i-1] = first, num[i..j-1] = second; start comparing from j
    private boolean isValid(String num, int aStart, int i, int j) {
        BigInteger a = new BigInteger(num.substring(aStart, i));
        BigInteger b = new BigInteger(num.substring(i, j));
        int n = num.length();
        int k = j;
        int count = 2;

        while (k < n) {
            BigInteger c = a.add(b);
            String s = c.toString();

            // if next chunk doesn't match c, sequence fails
            if (!num.startsWith(s, k)) return false;

            // advance window
            k += s.length();
            a = b;
            b = c;
            count++;
        }

        // must contain at least 3 numbers
        return count >= 3 && k == n;
    }
}

public class Main {
    public static void main(String[] args) {
        Solution sol = new Solution();

        // Provided examples
        run("112358", true, sol);
        run("199100199", true, sol);

        // Edge cases
        run("000", true, sol);            // 0,0,0
        run("101", true, sol);            // 1,0,1
        run("1023", false, sol);          // leading zero would break
        run("1203", false, sol);
        run("0235813", false, sol);       // cannot start with leading zero
        run("198019823962", true, sol);   // classic additive example
        run("1", false, sol);
        run("12", false, sol);

        // Very large numbers (overflow-safe due to BigInteger)
        // "123581321345589144" => 1,2,3,5,8,13,21,34,55,89,144
        run("123581321345589144", true, sol);

        // Random negatives/invalid (digits only rule)
        List<String> invalids = Arrays.asList("1a2", "++", "");
        for (String s : invalids) {
            System.out.printf("num=%s => %s (expected: false)%n", s, isDigits(s) ? sol.isAdditiveNumber(s) : false);
        }
    }

    private static void run(String num, boolean expected, Solution sol) {
        boolean got = isDigits(num) && sol.isAdditiveNumber(num);
        System.out.printf("num=%s => %s (expected: %s)%n", num, got, expected);
    }

    private static boolean isDigits(String s) {
        if (s == null || s.isEmpty()) return false;
        for (int i = 0; i < s.length(); i++) {
        }
        return true;
    }
}