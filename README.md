## User Hierarchy
* README.md
* usersHierarchy.py
* unitTest.py
## How To Run
* install pytest
> pip install pytest
* run test case
> python unitTest.py
```
============================= test session starts =============================
platform darwin -- Python 3.8.3, pytest-5.4.3, py-1.9.0, pluggy-0.13.1
rootdir: /Users/tengluntan/Documents/GitHub/User_Hierarchy
collected 2 items

unitTest.py ..

============================== 2 passed in 0.10s ==============================
```
## Algorithm
```
# use bfs to to solve this problem
# the eligible roll and user will be removed from the rolls and users, improving program efficiency
import copy
