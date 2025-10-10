class Solution {
    public List<Integer> findMinHeightTrees(int n, int[][] edges) {
        if (n == 1) return Collections.singletonList(0);

        List<List<Integer>> graph = new ArrayList<>(n);
        int[] degree = new int[n];
        for (int i = 0; i < n; i++) 
            graph.add(new ArrayList<>());

        for (int[] e : edges) {
            int u = e[0], v = e[1];

            graph.get(u).add(v);

            graph.get(v).add(u);

            degree[u]++; degree[v]++;
        }

        Deque<Integer> leaves = new ArrayDeque<>();

        for (int i = 0; i < n; i++) {
            if (degree[i] == 1) {
                leaves.add(i);
            };
         };

        int remaining = n;

        while (remaining > 2) {
            int size = leaves.size();
            remaining -= size;
            
            for (int s = 0; s < size; s++) {
                int leaf = leaves.poll();
                for (int nei : graph.get(leaf)) {
                    if (--degree[nei] == 1) 
                        leaves.add(nei);
                }
            }
        }

        return new ArrayList<>(leaves);
    }
}