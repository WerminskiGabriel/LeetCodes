class Solution {
    public int removeDuplicates(int[] nums) {
        
        int last = -10001;
        boolean lastDoubleFlag = false;

        int idx = 0;
        for( int i = 0; i < nums.length; i++ ){
            if( nums[i] > last ) {
                last = nums[i];
                nums[idx] = nums[i];
                idx++;
                lastDoubleFlag = false;
            }
            else if( nums[i] == last && !lastDoubleFlag){
                nums[idx] = nums[i];
                idx++;
                lastDoubleFlag = true;
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