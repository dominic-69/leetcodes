class Solution(object):
    def defangIPaddr(self, address):
        new = ""
        for i in address:
            if i ==".":
                new +="[.]"
            else:
                new +=i
        return new
        """
        :type address: str
        :rtype: str
        """
        