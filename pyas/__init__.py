from ctypes import CFUNCTYPE, addressof, c_void_p as void
from tempfile import NamedTemporaryFile
from binascii import unhexlify
from mmap import mmap
from os import system
buffer = []
def __strip_comments(string, separators):
	for sep in separators: string = string.split(sep)[0]
	return string
def function(asm: str, raw = True):
	global buffer
	if raw: asm_parsed = unhexlify(str().join(chunk.strip() for l in asm.splitlines() for chunk in __strip_comments(l, ["#", ";", "//"]).split()))
	else:
		temp = NamedTemporaryFile(mode='w+t', delete=False)
		temp.write(asm)
		temp.close()
		name = temp.name
		if not system("nasm -felf {} -o {}.o".format(name, name)):
			system("objcopy -O binary {}.o {}.hex".format(name, name))
			try: asm_parsed = open("{}.hex".format(name), "rb").read()
			except FileNotFoundError: return None
		else: return None
	buffer += [mmap(-1, length=max(len(asm_parsed)//2, 8), prot=7)]
	for byte in asm_parsed: buffer[-1].write_byte(byte)
	return CFUNCTYPE(void)(addressof(void.from_buffer(buffer[-1])))
