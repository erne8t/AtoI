class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.lstrip() # remove all spaces on left
        if str=='': return 0 # empty string case returns 0
        sign = 0 # 0 is defined as positive, by default sign is 0
        if str[0]=='+':
            try:
                str = str[1:]
            except IndexError:
                return 0
        elif str[0]=='-':
            try:
                sign = 1; str = str[1:] # 1 is defined as negative
            except IndexError:
                return 0
        x = ''
        str += 'e' # this is a trick to make sure the following while loop runs to the end
        while str[0]>='0' and str[0]<='9': # make sure all digits
            x += str[0]
            str = str[1:] # this is why str needs an arbitrary chr(e.g. 'e') at end

        if x=='': return 0 # if empty, return 0

        x.lstrip('0') # remove 0's at beginning
        # test before conversion
        if len(x)>10 and sign==0: return 2147483647 # positive overflow
        elif len(x)>10 and sign==1: return -2147483648
        elif sign==0 and len(x)==10 and x>'2147483647': return 2147483647 # positive overflow
        elif sign==1 and len(x)==10 and x>'2147483648': return -2147483648 # negative overflow

        if sign==1: return -int(x)
        else: return int(x)
