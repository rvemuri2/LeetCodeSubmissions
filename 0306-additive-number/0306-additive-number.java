import java.math.BigInteger;


class Solution {
    public boolean isAdditiveNumber(String num) {
        int n = num.length();
        for (int i = 1; i <= n - 2; i++) {
            if (num.charAt(0) == '0' && i > 1) 
                break;
            for (int j = i + 1; j <= n - 1; j++) {
                if (num.charAt(i) == '0' && j - i > 1) 
                    break;

                if (isValid(num, 0, i, j)) {
                    return true;
                }
            }
        }
        return false;
    }

    private boolean isValid(String num, int aStart, int i, int j) {
        BigInteger a = new BigInteger(num.substring(aStart, i));
        BigInteger b = new BigInteger(num.substring(i, j));
        int n = num.length();
        int k = j;
        int count = 2;

        while (k < n) {
            BigInteger c = a.add(b);
            String s = c.toString();
            if (!num.startsWith(s, k)) {
                return false;
            }
            k += s.length();
            a = b;
            b = c;
            count++;
        }
        return count >= 3 && k == n;
    }
}