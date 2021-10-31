from ctypes import CFUNCTYPE, addressof, c_void_p as void
from binascii import unhexlify
from mmap import mmap
buffer = []
def function(asm: str):
	global buffer
	strip_comments = lambda a, b: [ a := a.split(c)[0] for c in b ]
	asm_parsed = str().join(chunk.strip() for l in asm.splitlines()
	for chunk in strip_comments(l, [ "#", ";", "//" ])[-1].split())
	buffer += [mmap(-1, length=max(len(asm_parsed)//2, 8), prot=7)]
	for byte in unhexlify(asm_parsed) : buffer[-1].write_byte(byte)
	return CFUNCTYPE(void)(addressof(void.from_buffer(buffer[-1])))
