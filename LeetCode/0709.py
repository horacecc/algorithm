class Solution:
    def toLowerCase(self, str: str) -> str:
        ans = ""
        for x in list(str):
            if 97 <= ord(x) <= 122 or 65 <= ord(x) <= 90:
                ans += chr(ord(x) % 97 % 65+97)
            else:
                ans += x
        return ans

