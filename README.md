# About our Team
2019.11.05 :octocat: #L7

* * *

## Index
- [Members](#Members)
- [About project](#project)
- [Tests](#test)
  - [Use unittest](#unittest)
  - [Use pytest](#pytest)
- [Install](#install)
- [Uninstall](#uninstall)
- [Activities](#Activities)
  - [Code Contribution](#code)
  - [Creating Documents](#doc)
  - [Creating Team Static Page](#page)
- [New or Edited Files](#file)
  - [New Algorithms](#algorithm)
  - [Another Files](#another)
- [Wiki](#wiki)
  
* * *

## <div id="Members">Members</div>
| Name | Major/Grade | GithubID |
| :---: | :---: | :---: |
| 나종명 | 컴퓨터공학과/14   | D-Sinus |
| 조현진 | 컴퓨터공학과/16   | guswh11 |
| 박찬혁 | 소프트웨어학과/19 | WithM2  |
| 손병호 | 소프트웨어학과/19 | sonho00 |
| 장진우 | 소프트웨어학과/19 | doldam0 |

* * *

## <div id = "project">About Project</div>
Our project based on [algorithms](https://github.com/keon/algorithms).

[![PyPI version](https://badge.fury.io/py/algorithms.svg)](https://badge.fury.io/py/algorithms)
[![Open Source Helpers](https://www.codetriage.com/keon/algorithms/badges/users.svg)](https://www.codetriage.com/keon/algorithms)
[![Build Status](https://travis-ci.org/keon/algorithms.svg?branch=master)](https://travis-ci.org/keon/algorithms)
[![Coverage Status](https://coveralls.io/repos/github/keon/algorithms/badge.svg?branch=master)](https://coveralls.io/github/keon/algorithms?branch=master)
![algorithms](https://raw.githubusercontent.com/keon/algorithms/master/docs/source/_static/logo/logotype1blue.png)

## Pythonic Data Structures and Algorithms

Minimal and clean example implementations of data structures and algorithms in Python 3.

* * *

## <div id = "test">Tests</div>

### <div id = "unittest">Use unittest</div>
For running all tests write down:

    $ python3 -m unittest discover tests

For running some specific tests you can do this as following (Ex: sort):

    $ python3 -m unittest tests.test_sort

### <div id = "pytest">Use pytest</div>
For running all tests write down:

    $ python3 -m pytest tests

* * *

## <div id = "install">Install</div>
If you want to use the API algorithms in your code, it is as simple as:

    $ pip3 install algorithms

You can test by creating a python file: (Ex: use `merge_sort` in `sort`)

```python3
from algorithms.sort import merge_sort

if __name__ == "__main__":
    my_list = [1, 8, 3, 5, 6]
    my_list = merge_sort(my_list)
    print(my_list)
```

* * *

## <div id = "uninstall">Uninstall</div>
If you want to uninstall algorithms, it is as simple as:

    $ pip3 uninstall -y algorithms

* * *

## <div id="Activities">Activities</div>
### <div id="code">Code Contribution</div>
* Add Algorithms
> - Not on this project
> - To resolve issues
* Improve Algorithms
> - Increase algorithm speed 
> - Use less memory space

### <div id="doc">Creating Documents</div>
* How the algorithms work
* Association with the issue
* Compared to traditional algorithms

### <div id="page">Creating Team Static Page</div>
- Our static page summing-up our activities.
- This is our static page link

-> [가장 아름다운 파이썬 알고리즘 라이브러리](http://19-2-skku-oss.github.io/2019-2-OSS-L7/)

### **Screenshots**

<img src="https://user-images.githubusercontent.com/56295771/70390756-46a1da80-1a11-11ea-92fd-1b544a6ce2b5.PNG" width="50%"></img><img src="https://user-images.githubusercontent.com/56295771/70390757-473a7100-1a11-11ea-8235-db665dbc63bc.PNG" width="50%"></img>

* * *

## <div id="file">New or Edited Files</div>
### <div id="algorithm">New Algorithm List</div>
- [maths](https://github.com/19-2-SKKU-OSS/algorithms/tree/master/algorithms/maths)
  - [find_order_simple.py](https://github.com/19-2-SKKU-OSS/algorithms/tree/add_find_order/algorithms/maths/find_order_simple.py)
  - [find_primitive_root_simple.py](https://github.com/19-2-SKKU-OSS/algorithms/blob/add_find_primitive_root/algorithms/maths/find_primitive_root_simple.py)
  - [gcd.py](https://github.com/19-2-SKKU-OSS/algorithms/blob/add_gcd_bit/algorithms/maths/gcd.py)
  - [diffie_hellman_key_exchange.py](https://github.com/19-2-SKKU-OSS/algorithms/blob/add_diffie_hellman_key_exchange/algorithms/maths/diffie_hellman_key_exchange.py)
- [network_flow](https://github.com/19-2-SKKU-OSS/algorithms/tree/add_network_flow/algorithms/graph)
  - [maximum_flow.py](https://github.com/19-2-SKKU-OSS/algorithms/blob/add_network_flow/algorithms/graph/maximum_flow.py)
- [strings](https://github.com/19-2-SKKU-OSS/algorithms/blob/add_kmp/algorithms/strings)
  - [knuth_morris_pratt.py](https://github.com/19-2-SKKU-OSS/algorithms/blob/add_kmp/algorithms/strings/knuth_morris_pratt.py)
- [bfs](https://github.com/19-2-SKKU-OSS/2019-2-OSS-L7/blob/add_bfs_count_islands/algorithms/bfs)
  - [count_islands.py(add_bfs_count_islands)](https://github.com/19-2-SKKU-OSS/2019-2-OSS-L7/blob/add_bfs_count_islands/algorithms/bfs/count_islands.py)
- [dfs](https://github.com/19-2-SKKU-OSS/2019-2-OSS-L7/blob/add_dfs_maze_search/algorithms/dfs)
  - [maze_search.py(add_dfs_maze_search)](https://github.com/19-2-SKKU-OSS/2019-2-OSS-L7/blob/add_dfs_maze_search/algorithms/dfs/maze_search.py)
### <div id="another">Another Files</div>
- [maths](https://github.com/19-2-SKKU-OSS/2019-2-OSS-L7/blob/code/algorithms/maths)
  - [init.py(code)](https://github.com/19-2-SKKU-OSS/2019-2-OSS-L7/blob/code/algorithms/maths/__init__.py)
- [graph](https://github.com/19-2-SKKU-OSS/algorithms/blob/add_network_flow/algorithms/graph)
  - [init.py(add_network_flow)](https://github.com/19-2-SKKU-OSS/algorithms/blob/add_network_flow/algorithms/graph/__init__.py)
- [tests](https://github.com/19-2-SKKU-OSS/algorithms/blob/add_find_order/tests)
  - [test_maths.py(add_find_order)](https://github.com/19-2-SKKU-OSS/algorithms/blob/add_find_order/tests/test_maths.py)
  - [test_maths.py(add_gcd_bits)](https://github.com/19-2-SKKU-OSS/algorithms/blob/add_gcd_bit/tests/test_maths.py)
  - [test_graph.py(add_network_flow)](https://github.com/19-2-SKKU-OSS/algorithms/blob/add_network_flow/tests/test_graph.py)
- [bit](https://github.com/19-2-SKKU-OSS/algorithms/blob/code/algorithms/bit)
  - [init.py(code)](https://github.com/19-2-SKKU-OSS/algorithms/blob/code/algorithms/bit/__init__.py)
  - [trailing_zero.py(code)](https://github.com/19-2-SKKU-OSS/algorithms/blob/code/algorithms/bit/trailing_zero.py)

* * *

## <div id="wiki">Wiki</div>
  Our wiki page is [here](https://github.com/19-2-SKKU-OSS/2019-2-OSS-L7/wiki).
