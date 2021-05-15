class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        def common(a, b):
            # a, b: str
            i = 0
            substring = ''
            if len(a) <= len(b):
                while i < len(a) and a[i] == b[i]:
                    substring += a[i]
                    i += 1
            else:
                while i < len(b) and b[i] == a[i]:
                    substring += b[i]
                    i += 1
            return substring
        
        j = 0
        prefix = strs[j]
        while j < len(strs):
            prefix = common(prefix, strs[j])
            j += 1
        
        return prefix
        
