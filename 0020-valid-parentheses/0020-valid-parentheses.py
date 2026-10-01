class Solution:
    def isValid(self, s): return not __import__('functools').reduce(lambda st,c: st+c if c in '([{' else st[:-1] if st and st[-1]=={')':'(',']':'[','}':'{'}[c] else st+'#', s, '')