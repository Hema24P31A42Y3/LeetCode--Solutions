class Solution:
    def combinationSum(self, candidates, target):
        result = []

        def backtrack(start, current, remaining):
            # Target ki reach ayyam - oka combination dorikindi
            if remaining == 0:
                result.append(list(current))
                return

            # Remaining negative ayithe - ee dharilo vellakudadu
            if remaining < 0:
                return

            # start nunchi start chestham - enduku ante duplicate rakunda
            for i in range(start, len(candidates)):
                # Ee number ni teesuko
                current.append(candidates[i])
                # Ade number ni malli vadachu kabatti - i ne pampistham, i+1 kadu
                backtrack(i, current, remaining - candidates[i])
                # Backtrack - teesi, next number try chey
                current.pop()

        backtrack(0, [], target)
        return result