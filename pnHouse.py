#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution:
    input_value = ""
    def __init__(self):
        pass
    
    def main(self,input_value):
        iv_list = self._decode_nest_dict_to_list(input_value)
        rel = self._encode_list_to_nest_dict(iv_list)
        return rel
        
        
    def _decode_nest_dict_to_list(self,d):
        if len(d.keys()) == 0:
            return list()
        ll = list()
        t_dict = d

        while True:
            if type(t_dict) is not type(dict()):
                ll.append(t_dict)
                break
            temp = list(t_dict.keys())
            ll.append(temp[0])
            t_dict = t_dict[temp[0]]
        return ll
            
    
    def _encode_list_to_nest_dict(self,ll):

        if len(ll) == 0:
            return dict()

        rel = dict()
        t_val = ll[0]
        for i in range(1,len(ll),1):
            rel = {ll[i]:t_val}
            t_val = rel
        return rel

import unittest
class testSolution(unittest.TestCase):
    # Input:
    input_value = [
                   {'hired': {'be': {'to': {'deserve': 'I'}}}},
                   {'?':{'you':{'are':'How'}}},
                   {}
                  ]

    iv_list = [
               ['hired', 'be', 'to', 'deserve', 'I'],
               ['?','you','are','How'],
               []
              ]
    # Output:
    output_value = [
                    {'I': {'deserve': {'to': {'be': 'hired'}}}},
                    {'How':{'are':{'you':'?'}}},
                    {}
                   ]
    
    sol = Solution()
    
    def test_main(self):
        for i in range(len(self.input_value)):
            self.assertDictEqual(self.sol.main(self.input_value[i]),self.output_value[i])
    def test_decode_nest_dict_to_list(self):
        for i in range(len(self.input_value)):
            self.assertListEqual(self.sol._decode_nest_dict_to_list(self.input_value[i]),self.iv_list[i])
    def test_encode_list_to_nest_dict(self):
        for i in range(len(self.iv_list)):
            self.assertDictEqual(self.sol._encode_list_to_nest_dict(self.iv_list[i]),self.output_value[i])

if __name__ == "__main__":
    unittest.main(verbosity=2)