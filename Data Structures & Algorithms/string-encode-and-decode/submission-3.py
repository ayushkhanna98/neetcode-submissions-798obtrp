class Solution:

    def encode(self, strs: List[str]) -> str:
        print("_|_".join(strs))
        if not strs: return "-1"
        return "_|_".join(strs)

    def decode(self, s: str) -> List[str]:
        if s == "-1": return []
        sp = s.split("_|_")
        print(sp)
        return sp
