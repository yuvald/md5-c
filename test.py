from ctypes import CDLL, c_char_p, create_string_buffer

def md5str(s: str) -> str:
    cmd5 = CDLL("./md5.so")
    cmd5.md5fromstr.argtypes = [c_char_p, c_char_p]
    # Create mutable memory buffer for the c md5 function result 
    result = create_string_buffer(b'\000' * 17)
    cmd5.md5fromstr(s.encode(), result)
    return result.value.hex()


def md5str(s: str) -> str:
    cmd5 = CDLL("./md5.so")
    cmd5.md5fromstr.argtypes = [c_char_p, c_char_p]
    result = create_string_buffer(b'\000' * 17)
    cmd5.md5fromstr(s.encode(), result)
    return result.value.hex()


if __name__ == '__main__':
    for c in "ABCD":
        print(md5str(c*3))

