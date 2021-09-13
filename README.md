## User Hierarchy
* README.md
* UsersHierarchy.py
* test_getSubOrdinates.py
## How To Run
* install pytest
> pip install pytest
* run test case
> python test_getSubOrdinates.py
```
============================= test session starts =============================
platform win32 -- Python 3.7.6, pytest-6.2.5, py-1.10.0, pluggy-1.0.0
rootdir: D:\2021\Python\Users Hierarchy
collected 2 items

test_getSubOrdinates.py ..

============================== 2 passed in 0.10s ==============================
```
##Algorithm
```
# use bfs to to solve this problem
# the eligible roll and user will be removed from the rolls and users, improving program efficiency
import copy
