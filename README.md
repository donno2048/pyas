# pyas

Run machine code directly in Python

Have you ever realized you can't remember how to add numbers in Python but you **do** remember how to do it in assembly and convert it to machine code?

If the answer is yes this is the package for you, using `pyas` you will be able to run machine code directly from within Python!

```diff
- currently this only supports Linux
```

## Installation

### From PyPI

```sh
pip3 install pyas
```

### From GitHub

```sh
pip3 install git+https://github.com/donno2048/pyas
```

## Usage / Example

```py
from pyas import function
add_one = function(
    '8b c7'  # mov eax, edi
    '83 c0 01'  # add eax, 1
    'c3'  # ret
)
return_same = function(
    '''
    8b c7  # mov eax, edi
    c3  // ret
    '''
)

print(add_one(10), "=", return_same(10), "+ 1")
# output: 11 = 10 + 1

add_numbers = lambda i: function(
    '''
    8b c7  ; mov eax, edi
    83 c0 %.2x # add eax, i
    c3  // ret
    '''
    %i
)

print(add_numbers(4)(10), "=", "10 + 4")
# output: 14 = 10 + 4

```

Comments are noted with `;`, `#` and `//`
