class Solution(object):
    def countTrapezoids(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        MOD = 10**9 + 7
        from collections import defaultdict
        
        # Count points per y-level
        count_by_y = defaultdict(int)
        for x, y in points:
            count_by_y[y] += 1
        
        # Compute number of horizontal pairs per y-level
        vals = []
        for c in count_by_y.values():
            if c >= 2:
                pairs = c * (c - 1) // 2
                vals.append(pairs % MOD)
        
        # If fewer than 2 horizontal levels exist, no trapezoids
        if len(vals) < 2:
            return 0
        
        total = sum(vals) % MOD
        sq_sum = sum((v * v) % MOD for v in vals) % MOD
        
        # (total^2 - sum(v^2)) / 2
        ans = (total * total - sq_sum) % MOD
        ans = ans * pow(2, MOD - 2, MOD)  # modular division by 2
        
        return ans % MOD