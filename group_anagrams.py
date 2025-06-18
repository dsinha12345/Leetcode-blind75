class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash1 = {}
        for i in strs:
            result = hash(tuple(sorted(i)))
            if result in hash1:
                hash1[result].append(i)
            else:
                hash1[result] = [i]
        print(hash1)
        final_list = []
        for key in hash1:
            final_list.append(hash1[key])
        return final_list
