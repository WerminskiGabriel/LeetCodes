class Solution {
    public String longestCommonPrefix(String[] strs) {
        
        if( strs == null || strs.length == 0 ){
            return "";
        }

        String res = strs[0];
        for( int i = 0 ; i < res.length() ; i ++ ){

            for( int j = 1 ; j < strs.length ; j++ ){
            
                if (  strs[j].length() <= i || res.charAt(i) !=  strs[j].charAt( i )  ){
                    return res.substring( 0 , i );
                }
            }
        }

        return res;
    }
}