class Solution {
    public int removeDuplicates(int[] nums) {
        
        int last = -101;
        int idx = 0;
        for( int i = 0; i < nums.length; i++ ){
            if( nums[i] > last ) {
                last = nums[i];
                nums[idx] = nums[i];
                idx++;
            }
        }
        int res = nums.length;
        while( idx < nums.length ) {
            nums[idx] = 0;
            idx++;
            res--;
        }

        return res;
    }

}