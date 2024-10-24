# -*- coding: utf-8 -*-
"""
EXERCISE 8
SIMPLE SEARCH
"""

Names = ["Jake","Zac","Ian","Ron","Sam","Dave"]
search_name = "Sam"
if search_name in Names:
    print(f"{search_name} was found in the list")
else:
    print(f"{search_name} was not found in the list")