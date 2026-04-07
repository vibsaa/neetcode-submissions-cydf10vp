class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # #number of char and char type shud match
        # s_count ={}
        # t_count ={}
        # if len(s)!=len(t):
        #     return False
        
        # for i in range(len(s)):
        #     s_count[s[i]] = 1 + s_count.get(s[i],0) 
        #     t_count[t[i]] = 1 + t_count.get(t[i],0) 

        # for c in s_count:
        #     if s_count[c] != t_count.get(c,0):
        #         return False
        # return True


        #or
        return Counter(s) == Counter(t)


        #or , we can sort the string and compare. if anagram they shud be the same.
        # assuming sorting algo doesnt take any space o(1) then it can check for anagram without any space needs



            


                

        