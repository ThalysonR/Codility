class Solution {
    public int solution(int N) {
        int bgapCount = 0;
        int bgapMax = 0;
        
        String binary = Integer.toBinaryString(N);
        
        for (char c: binary.toCharArray()) {
            if (c == '1') {
                bgapMax = bgapMax > bgapCount ? bgapMax : bgapCount;
                bgapCount = 0;
            } else {
                bgapCount++;
            }
        }
        return bgapMax;
    }
}
