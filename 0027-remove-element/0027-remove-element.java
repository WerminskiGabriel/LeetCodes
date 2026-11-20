class Solution {
    public int removeElement(int[] nums, int val) {
        
        int j = 0;
        for( int i = 0; i< nums.length; i++ ){
            if( val != nums[i] ){
                nums[j] = nums[i];
                j++;
            }
        }

        int res = j;
        while( j < nums.length ) {
            nums[j] = 0;
            j++;
        }

        return res;

    }
}