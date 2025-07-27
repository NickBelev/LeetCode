class PascalsTriangle {
    public List<List<Integer>> generate(int numRows) {
        List<List<Integer>> triangle = new ArrayList<>(); // base case is a triangle where numRows = 1.  i = 0
        triangle.add(Collections.singletonList(1));
        
        // for second row onwards
        for (int i = 1; i < numRows; i++) {
            List row = new ArrayList<Integer>(); // build current row

            row.add(1); // 0th index is always a 1... strategy to avoid

            for (int x = 0; x < i - 1; x++) {
                row.add(triangle.get(i - 1).get(x) + triangle.get(i - 1).get(x + 1)); // sum up two adjacent values in the row above, above the current index
            }

            row.add(1); // ith row at index i is always a 1

            triangle.add(row);

        }

        return triangle;

    }
}
