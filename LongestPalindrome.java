class LongestPalindrome {
    public String longestPalindrome(String s) {
        String pal = "";
        int pal_len = 0;

        // Odd-length palindromes
        for (int i = 0; i < s.length(); i++) {
            int l = i;
            int r = i;
            while (l >= 0 && r < s.length() && (s.charAt(l) == s.charAt(r))) {
                if ((r - l + 1) > pal_len) {
                    pal = s.substring(l, r + 1);
                    pal_len = pal.length();
                }
                l--;
                r++;
            }
        }

        // Even-length palindromes
        for (int i = 0; i < s.length() - 1; i++) {
            int l = i;
            int r = i + 1;
            while (l >= 0 && r < s.length() && (s.charAt(l) == s.charAt(r))) {
                if ((r - l + 1) > pal_len) {
                    pal = s.substring(l, r + 1);
                    pal_len = pal.length();
                }
                l--;
                r++;
            }
        }

        return pal;
    }
}
