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
    private static boolean isDigits(String s) {
        return true;
    }
}