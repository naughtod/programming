class Solution {
    public void setZeroes(int[][] matrix) {
        Set<Integer> rowset = new HashSet<Integer>();
        Set<Integer> colset = new HashSet<Integer>();
        
        // collect rows and columns to zero
        for (int i=0;i<matrix.length;i++) {
            for (int j=0;j<matrix[0].length;j++) {
                if (matrix[i][j] == 0) {
                    rowset.add(i);
                    colset.add(j);
                }
            }
        }
        
        // zero columns and rows
        Iterator<Integer> it = rowset.iterator();
        while(it.hasNext()) {
            int row = it.next();
            for (int j=0;j<matrix[0].length;j++)
                matrix[row][j] = 0;
        }
        
        Iterator<Integer> it_ = colset.iterator();
        while(it_.hasNext()) {
            int col = it_.next();
            for (int i=0;i<matrix.length;i++)
                matrix[i][col] = 0;
        }
    }
}
