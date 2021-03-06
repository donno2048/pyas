# pyas

Run machine code, assembly and webassembly directly in Python.

Have you ever realized you can't remember how to add numbers in Python but you **do** remember how to do it in assembly?

If the answer is yes this is the package for you, using `pyas` you will be able to run machine code, assembly and webassembly directly from within Python!

> **Warning**
> currently this only supports Linux and pyscript

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
    '\0asm\1\0\0\0\1\6\1`\1'
    '\x7f\1\x7f\3\2\1\0\7'
    '\x0b\1\7add_one\0\0\n\t'
    '\1\7\0\x20\0A\x01j\x0b'
    , func_name = 'add_one')
print(f"{add_one(10)} = {add_one(9)} + 1")
```

View [online](https://donno2048.github.io/pyas/)
