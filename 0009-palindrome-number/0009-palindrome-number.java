class Solution {
    public boolean isPalindrome(int x) {
        if( x < 0 ){
            return false ;
        }

        int oldX = x;
        int newX = 0;

        while( x > 0 ) { 
            newX = newX * 10 + x % 10;
            x /= 10;
        }

        return oldX == newX;


    }
}