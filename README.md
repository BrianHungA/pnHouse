# pnHouse
pnHouse interview test
- The pnHouse.py is including two part of classes
  - Solution:  
    - main(input_value):  
    Input a nested input_value. The main function will output the reversed nested value.  
    e.g.  
    input_value = {'hired': {'be': {'to': {'deserve': 'I'}}}}]  
    output_value = {'I': {'deserve': {'to': {'be': 'hired'}}}}
    - _decode_nest_dict_to_list(d):  
    Input a nested input_value, d. This function will output the string list of nested input_value.  
    e.g.  
    input_value = {'hired': {'be': {'to': {'deserve': 'I'}}}}]  
    output_list = ['hired', 'be', 'to', 'deserve', 'I']
    - _encode_list_to_nest_dict(ll):  
    Input a string list, ll. This function will output a nested dict from reversed ll.  
    e.g.  
    input_list = ['hired', 'be', 'to', 'deserve', 'I']  
    output_dict = {'I': {'deserve': {'to': {'be': 'hired'}}}}
  - testSolution:  
    Use this to complete the unit test from each function of class Solution.  
    The coverage rate is 100%
