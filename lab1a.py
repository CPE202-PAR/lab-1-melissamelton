# Melissa Melton
# CPE 202 - Lab 1a

from typing import Optional
from typing import List

#Maybe_List -> Maybe_Int
def max_list_iter(int_list: Optional[List]) -> Optional[int]:
    """finds the max of a list of numbers and returns the value (not the index)
   If int_list is empty, returns None. If list is None, raises ValueError"""
    if int_list is None:
        raise ValueError
    elif len(int_list) == 0:
        return None
    elif len(int_list) == 1:
        return int_list[0]
    else:
       maxVal = int_list[0]
       for value in int_list:
            if value > maxVal:
                maxVal = value
       return value

# Maybe_List -> Maybe_List
def reverse_list(int_list: Optional[List]) -> Optional[List]:
   """reverses a list of numbers and returns the reversed list
   If list is None, raises ValueError"""
   if int_list is None:
      raise ValueError
   elif len(int_list) == 0:
      return []
   else:
      return [int_list[-1]] + reverse_list(int_list[:-1])


# Maybe_List -> None
def reverse_list_mutate(int_list: Optional[List]) -> None:
   """reverses a list of numbers, modifying the input list, returns None
   If list is None, raises ValueError"""
   if isinstance(int_list, list):
       if len(int_list) == 0:
           int_list = int_list
       elif len(int_list) > 0:
           mod_list = [int_list[-1]] + reverse_list(int_list[:-1])
           for i in range(len(mod_list)):
              int_list[i] = mod_list[i]
   else:
       raise ValueError