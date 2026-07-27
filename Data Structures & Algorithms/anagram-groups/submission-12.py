class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        visited = [False] * len(strs)
        ans = []

        for i in range(len(strs)):

            if visited[i]:
                continue

            group = [strs[i]]
            visited[i] = True

            for j in range(i + 1, len(strs)):

                if not visited[j] and sorted(strs[i]) == sorted(strs[j]):
                    group.append(strs[j])
                    visited[j] = True

            ans.append(group)

        return ans