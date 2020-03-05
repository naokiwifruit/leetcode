# Wrong Answer

class Solution:
    def isValid(self, s: str) -> bool:
        par = ['(', ')']
        brace = ['{', '}']
        bracket = ['[', ']']
        characters = [par, brace, bracket]
        
        if len(s) % 2 == 0:
            return False
        
        for chars in characters:
            if len(set(s) - set(chars)) % 2 != 0:
                return False
            
            left_idx = s.index(chars[0])
            right_idx = s.index(chars[1])
            if left_idx > right_idx:
                return False
            
            for chars2 in  characters.remove(chars):
                s_inside = s[left_idx+1:right_idx]
                left_idx = s_inside.index(chars2[0])
                right_idx = s_inside.index(chars2[1])
                if left_idx > right_idx:
                    return False
                
        return True
