import base64
class Solution:

    def encode(self, strs: list[str]) -> str:
        enc = ""
        for s in strs:
            enc+=base64.b64encode(s.encode()).decode()+"/0"
        return enc
        
    def decode(self, s: str) -> list[str]:

        sdec = s.split("/0")
        final = []
        for t in sdec:
            final.append(base64.b64decode(t).decode())
        final.pop(len(final)-1)

        return final

    