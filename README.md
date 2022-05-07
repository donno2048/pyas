# pyas

Run machine code, assembly and webassembly directly in Python.

Have you ever realized you can't remember how to add numbers in Python but you **do** remember how to do it in assembly?

If the answer is yes this is the package for you, using `pyas` you will be able to run machine code, assembly and webassembly directly from within Python!

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

### Machine code

Comments are noted with `;`, `#` and `//`

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

add_numbers = lambda i, val: function(
    '''
    8b c7  ; mov eax, edi
    83 c0 %.2x # add eax, i
    c3  // ret
    '''
    %i,
    val # every value after the first argument will be passed directly to the function if supplied
)

print(add_numbers(4, 10), "=", "10 + 4")
# output: 14 = 10 + 4

```

### Assembly

```py
from pyas import function
add_one = function(
    '''
    mov eax, edi
    add eax, 1
    ret
    ''',
    raw = False
)
return_same = function(
    '''
    mov eax, edi
    ret
    ''',
    raw = False
)

print(add_one(10), "=", return_same(10), "+ 1")
# output: 11 = 10 + 1

add_numbers = lambda i, val: function(
    '''
    mov eax, edi
    add eax, %d
    ret
    '''
    %i,
    val, # every value after the first argument will be passed directly to the function if supplied
    raw = False
)

print(add_numbers(4, 10), "=", "10 + 4")
# output: 14 = 10 + 4

```

## WebAssembly

pyas will automatically recognize running in a web browser and will run Webassembly, but you'll have to specify a `func_name`.

```py
from pyas import function
add_one = function(
    '''
    \x00asm\x01\x00\x00\x00\x01\x06\x01`
    \x01\x7f\x01\x7f\x03\x02\x01\x00\x07
    \x0b\x01\x07add_one\x00\x00\n\t\x01
    \x07\x00\x20\x00A\x01j\x0b
    ''', func_name = 'add_one')
print(str(add_one(10)) + "=" + str(add_one(9)) + "+ 1")
```
