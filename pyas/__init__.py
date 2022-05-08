from ctypes import CFUNCTYPE, addressof, c_void_p as void
from platform import system as platform
from binascii import unhexlify
buffer = []
def __strip_comments(string, separators):
	for sep in separators: string = string.split(sep)[0]
	return string
def function(asm: str, /, *args, raw = True, func_name = "main"):
	global buffer
	if args: return function(asm, raw=raw)(*args)
	if platform() == "Linux":
		from mmap import mmap
		if raw: asm_parsed = unhexlify(str().join(chunk.strip() for l in asm.splitlines() for chunk in __strip_comments(l, ["#", ";", "//"]).split()))
		else:
			from tempfile import NamedTemporaryFile
			from os import system
			temp = NamedTemporaryFile(mode='w+t', delete=False)
			temp.write(asm)
			temp.close()
			name = temp.name
			if not system("nasm -felf {} -o {}.o".format(name, name)): # this isn't cheating, I'm just checking what is the raw machine code to be able to use it
				system("objcopy -O binary {}.o {}.hex".format(name, name))
				try: asm_parsed = open("{}.hex".format(name), "rb").read()
				except FileNotFoundError: return None
			else: return None
		buffer += [mmap(-1, length=max(len(asm_parsed)//2, 8), prot=7)]
		for byte in asm_parsed: buffer[-1].write_byte(byte)
		ptr = addressof(void.from_buffer(buffer[-1]))
	elif platform() == "Emscripten":
		from pyodide_js._module import wasmTable
		from js import eval, WebAssembly
		from pyodide import to_js
		ptr = wasmTable.grow(1)
		wasmTable.set(ptr, eval(f"(_) => _.exports.{func_name}")(WebAssembly.Instance.new(WebAssembly.Module.new(to_js(asm.encode())))))
	else:
		return None
	return CFUNCTYPE(void)(ptr)
