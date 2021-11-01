from ctypes import CFUNCTYPE, addressof, c_void_p as void
from binascii import unhexlify
from mmap import mmap
buffer = []
def __strip_comments(string, separators):
	for sep in separators: string = string.split(sep)[0]
	return string
def function(asm: str):
	global buffer
	asm_parsed = str().join(chunk.strip() for l in asm.splitlines()
	for chunk in __strip_comments( l, [ "#", ";", "//" ] ).split())
	buffer += [mmap(-1, length=max(len(asm_parsed)//2, 8), prot=7)]
	for byte in unhexlify(asm_parsed) : buffer[-1].write_byte(byte)
	return CFUNCTYPE(void)(addressof(void.from_buffer(buffer[-1])))
