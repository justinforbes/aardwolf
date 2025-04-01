import librlers
from PIL import Image

bpp_2_bytes = {
	16: 2,
	24: 3,
	32: 4,
}

def rectconvert(width, height, bitsPerPixel, isCompress, data):
	if bitsPerPixel not in bpp_2_bytes:
		raise ValueError("bitsPerPixel value of %s is not supported!" % bitsPerPixel)
	try:
		image = librlers.bitmap_decompress(data, width, height, bitsPerPixel, int(isCompress))
	except Exception as e:
		print('Error decompressing bitmap data: %s' % e)
		print('Data: %s' % data)
		print('Width: %s' % width)
		print('Height: %s' % height)
		print('BitsPerPixel: %s' % bitsPerPixel)
		print('IsCompress: %s' % isCompress)
		raise
	return Image.frombytes('RGBA', [width, height], bytes(image))



# test data here
if __name__ == '__main__':
	#compressed_data = b'\x84\xff\xff\x00\x00\x00\x00\x00\x00\x00\x0c\x84\xff\xff\x00\x00\x00\x00\x00\x00'
	#width = 1
	#height = 13
	#bitsPerPixel = 16
	#isCompress = True
#
	#image = rectconvert(width, height, bitsPerPixel, isCompress, compressed_data)


	compressed_data = b'\x80\xcb\x9b\t]\x13\xbb\n\x92\n\xb1\x1a\xb3\x12\xb3\x12\xb3\x12\xb1\x1aW\\\xda\xa5\xdb\x95\xda\xa5\x95;\xd4\x1a\xb3\x12\x13\x1b\xb3\x12\xd4\x1a\xd4\x1a\x13\x1b\xd4\x1a\xd4\x1a\xd4\x1a\xf3"\x13\x1b\x14#\x14\x1b\x14#\x14\x1b\x14#\x14#5#\x14#5#\x14#T+5#U#5#T+U#T+U#u+u+u+u+u+u+\x96+u+\x96+\x96+\x96+\x96+\xb63\x96+\xb63\x96+\xb73\xb63\xb63\xb63\x95;\xb63\xd73\xb73\xd73\xb73\xd73\xd73\xf8;\xd73\xf7;\xf7;\xf7;\xf7;\xf7;\xf7;VD\xf7;8<\xf8;9<\xf8;9<8<VD9<9<9<VD9<yD9<yD9<yD9<yDyDyDyD\xb9DyD\x9aDyD\x9aD\x9aD\x9aD\x9aD\xbaL\x9aD\xbaL\xbaL\xb9T\xbaL\xdaL\xbaL\xdaT\xdaT\xdaT\xdaT\xfa\\\xdaT\xfa\\\xfa\\\xfa\\\xfa\\\xfa\\\xfa\\\x1ae\x1ae\x1be\x1ae\x1be\x1be\x1am\x1be;m;m;m;m;u;u;u;u[u[u[u[u{}{}{}{}{}{}\x9b\x85{}\x9b\x85\x99\x85\x9b\x85\x9b\x85\x9b\x85\x9b\x85\xbb\x8d\x9b\x85\xbb\x8d\xbb\x8d\xbb\x8d\xbb\x8d\xdc\x8d\xbb\x8d\xdc\x8d\xdc\x8d\xfc\x95\xdc\x8d\xfc\x95\x1b\x8e\xfc\x95\xfc\x95\xfc\x95\xfc\x95\x1c\x9e\xfc\x95\x1c\x9e\xfc\x95\x1c\x9e\x1c\x9e\x1c\x9e\x1c\x9e\x1c\x9e\x1c\x9e<\xa6\x1c\x9e;\xae<\xa6<\xa6<\xa6<\xae<\xa6=\xae<\xae=\xae<\xae]\xae<\xae]\xae]\xae]\xae]\xae}\xb6]\xae}\xb6]\xae}\xb6}\xb6}\xb6}\xb6\xbc\xb6}\xb6\xbd\xbe}\xb6\x9c\xbe\x9d\xb6\xbd\xbe}\xb6\x9c\xbe\xbd\xbe\xbd\xbe\xbd\xbe\xbd\xbe\xbd\xbe\xbd\xbe\xe9\xbd\xbe\xdd\xc6\xf4~\x01\xbd\xbe\xdc\xbe\xbd\xbe\xdd\xc6\xbd\xbe\xbd\xbe\x9c\xbe\xbd\xbe\xbd\xbe\xbd\xbe\x9c\xbe\xbd\xbe\x9c\xbe\xbd\xbe\x9d\xb6\xbd\xbe}\xb6\xbd\xbe}\xb6\x9c\xbe}\xb6}\xb6}\xb6}\xb6}\xb6}\xb6]\xae}\xb6]\xae]\xae]\xae]\xae<\xae]\xae<\xae\\\xae<\xae=\xae<\xa6<\xae<\xa6<\xa6<\xa6;\xae\x1c\x9e<\xa6\x1c\x9e<\xa6\x1c\x9e\x1c\x9e\x1c\x9e\x1c\x9e\xfc\x95\x1c\x9e\xfc\x95\x1c\x9e\xfc\x95\xfc\x95\xfc\x95\xfc\x95\xfc\x95\xfc\x95\xdc\x8d\xfc\x95\xdc\x8d\xdc\x8d\xbb\x8d\xdc\x8d\xbb\x8d\xbb\x8d\xbb\x8d\xbb\x8d\x9b\x85\xbb\x8d\x9b\x85\x9b\x85\x9b\x85\x9b\x85\x9b}\x9b\x85{}\x9b}{}{}{}{}[u{}[u[u[m[u;u;u;m[m;m;m\x1am;m\x1am\x1am\x1ae\x1be\x1ae\x1ae\x1ae\x1ae\xfa\\\xfa\\\xfa\\\xfa\\\xfa\\\xfa\\\xdaT\xfa\\\xdaT\xdaT\xdaL\xdaT\xdaL\xdaL\xbaL\xdaL\xb9D\xdaD\x9aD\xdaD\x9aD\xb9D\x99<\xb9D\x99<\xb9DyD\xb9Dy<\x99<y<\x97Ly<y<y<y<X<y<X<VDX<X<8<VD8<8<8<8<\x174\x174\x174\x174\x174\xfb\x01\xf4\x00\x91\x00\x00\x00\x00\x00\x00\x00\x9b\t]\x13\xbb\n\xb3\x12\x92\n\xb3\x12\x92\n\xb3\x12\x96l\x18\x85\xb1\x1a\xd4\x1a\xd4\x1a\xdb\x95\x15L\xb1\x1a\xb3\x12W\\\xff\xff\xff\xff\xff\xff~\xe7\xd4\x1a\x18\x85\xff\xff\xbf\xf7W\\\x14\x1b\x18\x85\xff\xff\xbf\xf7xT\x14#:u\xff\xff\xff\xff\xda\xa5U#\x14#U#U#U#U#U#U#u+U#u+u+u+u+v+u+\x96+u+\x96+\x96+\x96+\x96+\x96+\x96+\xb63\x96+\xb63\xb63\xb73\xb63\xb73\xb73\xd73\xb73\xd73\xd73\xd73\xd73\xf7;\xf7;\xf7;\xf7;\xf7;\xf7;\xf8;\xf7;8<\xf7;9<\xf7;9<8<9<8<9<9<9<9<9<9<yD9<yD9<yDyDyDyDzDyD\x9aDyD\x9aDyD\x9aD\x9aD\x9aD\x9aD\xbaL\xb9D\xbaL\xbaL\xbaL\xbaL\xdaT\xb9T\xdaT\xb9T\xfa\\\xb9T\xfa\\\xd9d\xfa\\\xd9d\xfa\\\xfa\\\x1be\xd9d\x1ae\x1ae\x1be\x1be\x1be\x1be;m\x1be;m;m;u;m;u;u[u;u[u[u{}[u{}{}{}{}z\x85{}\x9b\x85{}\x9b\x85\x9b\x85\x9b\x85\x9b\x85\x9b\x85\x9b\x85\xbb\x8d\xbb\x8d\xbb\x8d\xbb\x8d\xdc\x8d\xbb\x8d\xdc\x8d\xdc\x8d\xdc\x8d\xdc\x8d\xfc\x95\xdb\x95\xfc\x95\xfc\x95\xfc\x95\xfc\x95\xfc\x95\xfc\x95\x1c\x9e\xfc\x95\x1c\x9e\xfc\x95\x1c\x9e\x1c\x9e\x1c\x9e\x1c\x9e<\xa6\x1c\x9e<\xa6<\xa6<\xa6<\xa6<\xae<\xa6<\xae<\xae]\xae<\xae]\xae\\\xae]\xae]\xae]\xae]\xae}\xb6\\\xaeh}\xb6\x8a\xbc\xb6\x9d\xb6\x9d\xb6}\xb6\xbd\xbe\x9d\xb6\xbd\xbe\x9c\xbe\xbd\xbe\x9c\xbeq\xbd\xbe\x94\x9c\xbe\xbd\xbe\xbd\xbe\xbd\xbe\x9c\xbe\xbd\xbe\xbd\xbe\xbd\xbe\x9c\xbe\xbd\xbe\x9c\xbe\xbd\xbe\x9d\xb6\xbd\xbe}\xb6\xbd\xbe}\xb6\x9c\xbe}\xb6\x9c\xbeh}\xb6\x80g]\xae}\xb6]\xae}\xb6\\\xae]\xae\\\xae\\\xae<\xae\\\xae<\xae<\xae<\xa6<\xae<\xa6<\xa6<\xa6<\xa6\x1c\x9e<\xa6\x1c\x9e\x1c\x9e\x1c\x9e\x1c\x9e\x1c\x9e\x1c\x9e\xfc\x95\x1c\x9e\xfc\x95\x1c\x9e\xfc\x95\xfc\x95\xfc\x95\xfc\x95\xdb\x95\xfc\x95\xdc\x8d\xdc\x8d\xdc\x8d\xdc\x8d\xbb\x8d\xdc\x8d\xbb\x8d\xbb\x8d\xbb\x8d\xbb\x8d\x9b\x85\x9b\x85\x9b\x85\x9b\x85\x9b\x85\x9b\x85{}\x9b\x85{}\x9b}{}{}{}{}[u{}[u[u;uZu;uZu;m;u;m;m\x1be;m\x1be\x1am\x1ae\x1ae\x1ae\x1ae\xfa\\\x1ae\xfa\\\x1ae\xd9d\xfa\\\xfa\\\xfa\\\xb9T\xdaT\xdaT\xdaT\xb9T\xdaL\xb9T\xdaL\xb9D\xdaD\xb9D\xdaD\x9aD\xb9D\x99<\xb9D\x99<\x9aD\x99<\xb9DyD\x99<y<\x99<y<\x99<y<y<X<y<X<VDX<X<X<X<749<8<8<748<\x1748<\xf7;\x174\xf7;\n\x80?\x92\n\xb3\x12\x92\n\xb3\x12\x95;\xdb\x95\x14+\x1e\xd7\x1d\xd7\x9c\xc6\xd4\x1a<\xae\xd4\x1a\xd4\x1a\xb3\x12\x9c\xc6\x18m\xd4\x1a\xd4\x1aT+\xbf\xf7W\\\x96l\x1e\xd7u+\xbf\xf7\xf8;\xd9d\x1d\xd7\x14#\xbf\xf7\xf6|t3~\xe7VDU#U#U#U#T+U#u+U#u+u+v+u+\x96+u+\x96+t3\x96+\x96+\x96+\x96+\xb63\x96+\xb63\x96+\xb63\xb63\xb73\xb63\xd73\xb73\xd73\xb73\xd73\xd73\xf7;\xd73\xf7;\xf7;\xf7;\xf7;\x174\xf7;8<\xf7;8<\xf8;8<\xf8;9<8<9<9<9<9<9<9<yD9<y<9<hyD\x800\x9aDyD\x9aDzD\xbaL\x9aD\x9aD\x9aD\xbaL\xbaL\xbaL\xbaL\xdaL\xbaL\xdaT\xb9T\xdaT\xdaT\xdaT\xdaT\xfa\\\xfa\\\xfa\\\xfa\\\xfa\\\xfa\\\x1ae\xfa\\\x1be\x1ae\x1be\x1ae\x1am\x1be;m\x1am:u;m;u;m;u;uZu;u{}[u{}[u{}{}{}{}\x9b\x85{}\x9b\x85{}\x9b\x85\x9b\x85\x9b\x85\x9b\x85\xbb\x8d\x9b\x85\xbb\x8d\xbb\x8d\xbb\x8d\xbb\x8d\xda\x8d\xbb\x8d\xdc\x8d\xdc\x8d\xdb\x95\xdc\x8d\xfc\x95\xfc\x95\xfc\x95\xfc\x95\xfc\x95\xfc\x95\x1c\x9e\xfc\x95h\x1c\x9ef<\xa6\x9a<\xae<\xa6\\\xae<\xae\\\xae<\xae]\xae]\xae]\xae\\\xae}\xb6]\xae}\xb6]\xae}\xb6}\xb6}\xb6}\xb6\x9c\xbe}\xb6\x9d\xb6}\xb6\xbd\xbe\x9d\xb6\x9c\xbe\xbc\xb6h\xbd\xbe\x83\xdd\xc6\xbd\xbe\xbd\xbe\xe7\xbd\xbe\xdd\xc6\x03\x80\x7f\xdd\xc6\xbd\xbe\xbd\xbe\xbd\xbe\xdc\xbe\xbd\xbe\xbd\xbe\x9c\xbe\xbd\xbe\x9c\xbe\xbd\xbe\x9d\xb6\xbd\xbe\x9d\xb6\xbd\xbe\x9d\xb6\xbd\xbe}\xb6\x9c\xbe}\xb6\xbc\xb6}\xb6}\xb6}\xb6}\xb6]\xae}\xb6]\xae}\xb6]\xae]\xae\\\xae]\xae<\xae\\\xae<\xae\\\xae<\xae<\xae<\xa6<\xa6<\xa6<\xa6\x1c\x9e<\xa6\x1c\x9e\x1c\x9e\x1c\x9e\x1c\x9e\x1c\x9e\x1c\x9e\xfc\x95\x1c\x9e\xfc\x95\x1c\x9e\xfc\x95\xfc\x95\xfc\x95\xfc\x95\xdb\x95\xfc\x95\xdc\x8d\xdb\x95\xdc\x8d\xdc\x8d\xbb\x8d\xdc\x8d\xbb\x8d\xbb\x8d\xbb\x8d\xbb\x8d\x9b\x85\xbb\x8d\x9b\x85\x9b\x85\x9b\x85\x9b\x85\x9b}\x9b\x85{}\x9b}{}{}Z}{}[u{}[uZ}[m[u;uZm;mZm;m;m\x1am;m\x1be\x1am\x1be\x1be\x1ae\x1ae\x1ae\x1ae\xfa\\\xfa\\\xfa\\\xfa\\\xdaT\xfa\\\xdaT\xdaT\xdaT\xdaT\xdaL\xdaL\xdaL\xdaL\xbaL\xdaD\xb9D\xdaD\x9aD\xb9D\x99<\xb9D\x99<\xb9D\x99<\xb9D\x99<\x99<y<\x97Ly<\x99<VD\x99<X<y<X<y<X<X<8<X<8<X<748<8<8<\x1748<\x174\x174\x0b\x805R"\xb3\x12\x92\n\xdb\x95\x14+\xdb\x95\x18\x85\xd4\x1a\x14+\xd4\x1a\xd9dW\\\xb3\x12\xd4\x1a\xb3\x12\x9c\xc6\xd9d\xd4\x1aW\\\x1d\xd7\xd4\x1a\x14\x1b\xbf\xf7\x96lz\xe6\x14#\x14\x1b\xbf\xf7u+\x1d\xd7\xb5C5#z\xe6W\\\x14#U#5#U#U#U#U#u+U#u+u+u+u+v+u+\x96+u+\x96+\x96+\x96+\x96+\x96+\x96+\xb63\xb63\xb63\xb63\xb73\xb63\xb73\xb63\xd73\xb73\xd73\xd73\xd73\xd73\xf7;\xf7;\xf7;\xf7;\xf8;\xf7;\xf8;\xf7;8<\xf7;8<\xf7;9<\xf8;h9<\x80Vy<9<yD9<yDyDyDyDyDyD\x9aDyD\x9aDyD\x9aDzD\x9aD\x9aD\xbaL\x9aD\xbaL\xbaL\xb9T\xbaL\xdaT\xb9T\xdaT\xb9T\xdaT\xb9T\xfa\\\xb9T\xfa\\\xfa\\\xfa\\\xd9d\x1ae\xfa\\\x1be\x1ae\x1be\x1be\x1am\x1be;m\x1be;m;m;u;u;u;u[u;u[u;uZ}[u{}Z}{}{}\x9b}{}\x9b\x85{}\x9b\x85\x9b\x85\x9b\x85\x9b\x85\xbb\x8d\x9b\x85\xbb\x8d\xbb\x8d\xbb\x8d\xbb\x8d\xdc\x8d\xda\x8d\xdc\x8d\xdc\x8d\xdc\x8d\xdc\x8d\xfc\x95\xdb\x95\xfc\x95\xfc\x95\xfc\x95\xdb\x95\xfc\x95\xfc\x95\x1c\x9e\xfc\x95\x1c\x9e\x1c\x9e\x1c\x9e\xda\xa5\x1c\x9e\x1c\x9e<\xa6;\x9e<\xa6<\xa6<\xae<\xa6<\xae<\xae<\xae<\xae]\xae<\xae]\xae;\xae]\xae]\xae}\xb6;\xae}\xb6\\\xaeh}\xb6\x01\x80\x10}\xb6\x9d\xb6}\xb6\xbd\xbe\x9d\xb6\xbd\xbe\x9c\xc6\xbd\xbe\x9c\xbe\xbd\xbe\xbd\xbe\xbd\xbe\x9c\xc6\xbd\xbe\xbd\xbe\xdd\xc6\x9c\xc6\xbd\xbe\xbd\xbe\xdd\xc6\xbd\xbe\xbd\xbe\xbd\xbe\xdd\xc6\xbd\xbe\xbd\xbe\xbd\xbe\xdd\xc6\x9c\xc6\xbd\xbe\xbd\xbe\xbd\xbe\x9c\xbe\xbd\xbe\xbd\xbe\xbd\xbe\x9c\xbe\xbd\xbe\x9c\xbe\xbd\xbe\x9c\xbe\xbd\xbe}\xb6\x9c\xbe}\xb6\x9c\xbe}\xb6\x9c\xbeh}\xb6\x80e;\xae]\xae\\\xae]\xae;\xae]\xae<\xae\\\xae<\xa6<\xae<\xae=\xae<\xa6<\xa6<\xa6<\xa6\x1c\x9e<\xa6\x1c\x9e<\xa6\x1c\x9e\x1c\x9e\x1c\x9e\x1c\x9e\xfc\x95\x1c\x9e\xfc\x95\x1c\x9e\xdb\x95\xfc\x95\xfc\x95\xfc\x95\xdb\x95\xfc\x95\xdc\x8d\xfc\x95\xdc\x8d\xdc\x8d\xda\x8d\xdc\x8d\xbb\x8d\xbb\x8d\xbb\x8d\xbb\x8d\x9b\x85\xbb\x8d\x9b\x85\x9b\x85\x9b\x85\x9b\x85{}\x9b\x85{}{}{}{}Zu{}[uZ}Zu[u;uZu;u;u;u;u;m;m\x1am;m\x1be\x1am\x1ae\x1be\x1ae\x1ae\xfa\\\x1ae\xfa\\\xfa\\\xfa\\\xfa\\\xb8\\\xfa\\\xb9T\xdaT\xb9T\xdaT\xb9T\xdaT\xbaL\xdaL\xb9D\xdaL\xb9D\xbaL\x9aD\xdaD\x99<\x9aD\x99<\x9aDyD\x99<yD\x99<y<\x99<y<\x99<X<y<X<y<X<X<X<X<74X<74X<748<748<\x17474\x174\x174\xf7;\x0b\x80\xc3\xb1\x1a\xb3\x12\xb3\x12\x99\x9d\xd4\x1a\xdb\x95\x18\x85\xd4\x1a\xf3"\xd4\x1aW\\W\\\xd4\x1a\xd4\x1a\xd4\x1a\xd4\x1a\x1e\xd7\x96lW\\\x9c\xc6\xf3"\x13\x1b~\xe7\xd9d\xdd\xc6\x14\x1b\x14#~\xe7\xf6;xT\x1e\xd7\x1d\xd7\xdb\x955#U#U#T+U#U#U#u+u+u+u+\xb4+u+\x96+u+\x96+\x96+\x96+\x96+\xb4+\x96+\xb63\x96+\xb63\xb63\xb73\xb63\x95;\xb63\xd73\xb73\xd73\xd73\xd73\xd73\xf8;\xd73\xf7;\xf7;\xf6;\xf7;\xf8;\xf7;8<\xf8;8<\xf8;9<8<9<8<VD9<9<9<9<9<y<9<yD9<yDyDyDyDyDyD\xb9DyD\x9aDyD\x9aD\x9aD\xbaL\x9aD\xbaL\x9aD\xbaL\xbaL\xdaL\xbaL\xdaL\xbaL\xdaT\xdaT\xdaT\xdaT\xfa\\\xdaT\xfa\\\xfa\\\xfa\\\xfa\\\xfa\\\xfa\\\x1be\x1ae\x1be\x1ae\x1am\x1be\x1am\x1be;u;m;m;m[m;u;u;u[u;u{}[u{}[u{}{}\x9b\x85{}\x9b\x85{}\x9b\x85\x99\x85\x9b\x85\x9b\x85\xba\x85\x9b\x85\xbb\x8d\x9b\x85\xbb\x8d\xbb\x8d\xbb\x8d\xbb\x8d\xdc\x8d\xdc\x8d\xdc\x8d\xdc\x8d\xfc\x95\xdc\x8d\xfc\x95\xfc\x95\xfc\x95\xfc\x95;\x9e\xfc\x95\x1c\x9e\xfc\x95\x1c\x9e\xfc\x95\x1c\x9e\x1c\x9e\x1c\x9e\x1c\x9e<\xa6\x1c\x9e<\xa6<\xa6<\xa6<\xa6<\xae<\xa6<\xae<\xae\\\xae<\xae]\xae]\xae]\xae]\xae}\xb6]\xae}\xb6]\xae}\xb6}\xb6}\xb6}\xb6\x9c\xbe}\xb6\x9c\xbe}\xb6\x9c\xbe}\xb6\xbd\xbe\x9d\xb6\x9c\xbe\x9c\xbe\xbd\xbe\xbd\xbe\xbd\xbe\xbd\xbe\xbd\xbe\xef\xbd\xbe\xdd\xc6\x01\x80w\xbd\xbe\x9c\xbe\xbd\xbe\x9c\xbe\xbd\xbe\x9c\xbe\xbd\xbe\x9c\xbe\xbd\xbe}\xb6\xbd\xbe}\xb6}\xb6}\xb6\x9c\xbe}\xb6}\xb6]\xae}\xb6]\xae}\xb6]\xae}\xb6]\xae]\xae<\xae]\xae=\xae\\\xae<\xae=\xae<\xa6<\xae<\xa6<\xa6<\xa6<\xa6\x1c\x9e;\xae\x1c\x9e\x1c\x9e\x1c\x9e\x1c\x9e\x1c\x9e\x1c\x9e\xfc\x95\x1c\x9e\xfc\x95\xfc\x95\xfc\x95\xfc\x95\xfc\x95\xfc\x95\xdc\x8d\xfc\x95\xdc\x8d\xdb\x95\xdc\x8d\xdc\x8d\xbb\x8d\xbb\x8d\xbb\x8d\xbb\x8d\x9b\x85\xbb\x8d\x9b\x85\xba\x85\x9b\x85\x9b\x85\x9b}\x9b\x85{}\x99\x85{}\x9b}{}{}[u{}[u[uZu[u;u[m;m[m;m;m\x1am;m\x1am;m\x1be;e\x1ae\x1ae\x1ae\x1ae\xfa\\\x1ae\xfa\\\xfa\\\xfa\\\xfa\\\xdaT\x1a]\xdaT\xdaT\xdaL\xdaT\xdaL\xdaL\xbaL\xdaL\xbaL\xdaD\x9aD\xdaD\x9aD\xb9D\x99<\xb9D\x99<\xb9DyD\xb9Dy<\x99<y<\x97Ly<\x99<X<y<X<y<X<VDX<X<8<VD8<8<8<8<\x174\x174\x174\x174\x07\x80\xb5\x9b\x01]\x13\xbb\n\x92\n\x92\n\xb3\x12\x92\nW\\\xd9d\xb5C~\xe7\xdb\x95\x9c\xbe\xd4\x1a\x99\x9d\xd4\x1a\xb3\x12\xd4\x1a\xb3\x12\xd4\x1a\xb5C\x1d\xd7\xb5C\x1d\xd7\xd4\x1a\x14\x1b\xbf\xf7W\\\x1d\xd7\x14#\x14\x1b\xbf\xf7v+\xd9d\x9c\xc6z\x85;\xaeU#\x14#U#U#U#U#U#U#u+U#u+u+u+u+v+u+\x96+u+\x96+\x96+\x96+\x96+\x96+\x96+\xb63\x96+\xb63\xb63\xb73\xb63\xb73\xb73\xd73\xb73\xd73\xd73\xf7;\xd73\xf7;\xf7;\xf7;\xf7;\xf7;\xf7;\xf8;\xf7;8<\xf7;9<\xf7;9<8<9<8<9<9<yD9<y<9<yD9<yDy<yDyDyDyDyDyD\x9aDyD\x9aDyD\x9aD\x9aD\xb9DzD\xbaL\xbaL\xbaL\xbaL\xdaT\xbaL\xdaT\xb9T\xdaT\xdaT\xfa\\\xb9T\xfa\\\xd9d\xfa\\\xfa\\\xfa\\\xfa\\\x1be\x1ae\x1ae\x1ae\x1be\x1be\x1am\x1be;m\x1am;m;m;u;u;u;u[u;u{}[u{}[u{}{}{}{}z\x85{}\x9b\x85{}\x9b\x85\x9b\x85\x9b\x85\x9b\x85\xbb\x8d\x9b\x85\xbb\x8d\xbb\x8d\xda\x8d\xbb\x8d\xdc\x8d\xbb\x8d\xdc\x8d\xdc\x8d\xfc\x95\xdc\x8d\xfc\x95\xfc\x95\xfc\x95\xfc\x95\xfc\x95\xfc\x95\x1c\x9e\xfc\x95\x1c\x9e\xda\xa5\x1c\x9e\xda\xa5\x1c\x9e\x1c\x9e<\xa6\x1c\x9e<\xa6<\xa6<\xa6<\xa6<\xae<\xa6=\xae<\xae\\\xae<\xae]\xae<\xae]\xae\\\xae}\xb6]\xae}\xb6]\xaeh}\xb6\x86\xbd\xbe}\xb6\x9d\xb6}\xb6\x9c\xbe\x9c\xbej\xbd\xbe\x83\xdd\xc6\xbd\xbe\xbd\xbe\xcf`x\x80~\xdc\xbe\xbd\xbe\xdd\xc6\x9c\xbe\xbd\xbe\xbd\xbe\xbd\xbe\x9c\xbe\xbd\xbe\xbd\xbe\xbd\xbe\x9c\xbe\xbd\xbe}\xb6\xbd\xbe}\xb6\xbd\xbe}\xb6\x9c\xbe}\xb6}\xb6}\xb6}\xb6}\xb6}\xb6]\xae}\xb6\\\xae]\xae\\\xae]\xae<\xae\\\xae<\xae\\\xae<\xae<\xae<\xa6<\xae<\xa6<\xa6<\xa6<\xa6\x1c\x9e<\xa6\x1c\x9e\x1c\x9e\x1c\x9e\x1c\x9e\xda\xa5\x1c\x9e\xfc\x95\x1c\x9e\xfc\x95\xfc\x95\xdb\x95\xfc\x95\xfc\x95\xfc\x95\xdc\x8d\xdb\x95\xdc\x8d\xdb\x95\xbb\x8d\xdc\x8d\xbb\x8d\xdc\x8d\xbb\x8d\xbb\x8d\x9b\x85\xbb\x8d\x9b\x85\x9b\x85\x9b\x85\x9b\x85{}\x9b\x85{}\x9b}{}{}{}{}[uZ}[u{};uZu[uZu;u;u;m;m\x1am;m\x1be\x1am\x1be\x1be\x1ae\x1ae\x1ae\x1ae\xfa\\\x1ae\xfa\\\xfa\\\xfa\\\xfa\\\xdaT\xdaT\xdaT\xdaT\xb9T\xdaT\xdaL\xdaL\xb9D\xdaL\xb9D\xdaD\x9aD\xb9D\x99<\xb9D\x99<\x9aD\x99<\xb9DyD\x99<y<\x99<y<\x99<y<y<X<y<X<VDX<X<X<X<8<9<8<8<748<\x17474\x174\x174\xf7;\x0b\x802\xb3\x12\x92\n\xb3\x12\xb3\x12\xdb\x95\x95;T+W\\T+W\\z\x85\xd4\x1a\xd4\x1a\xd4\x1a\xdd\xc6\x95;W\\>\xdf\x14\x1b\xbf\xf7W\\\x96l~\xe7\x14\x1b\xbf\xf7\xf8;\xd9d~\xe75#;\xae:}t3\xbf\xf7\xb5CU#U#U#U#T+U#u+U#u+u+v+u+\x96+u+\x96+u+\x96+\x96+\x96+\x96+\xb63\x96+\xb63\x96+\xb73\xb63\xb73\xb63\xd73\xb73\xd73\x95;\xd73\xd73\xf7;\xd73\xf7;\xf7;\xf7;\xf7;8<\xf7;8<\xf7;VD\xf8;8<\xf8;h9<\x80gyD9<yD9<yDyDyDyDyDyD\x9aDyD\x9aDzD\x9aDzD\xbaL\x9aD\x9aD\x9aD\xbaL\xbaL\xbaL\xbaL\xdaL\xbaL\xdaT\xb9T\xfa\\\xdaT\xfa\\\xdaT\xfa\\\xfa\\\xfa\\\xfa\\\x1ae\xfa\\\x1ae\xfa\\\x1be\x1ae\x1be\x1be;m\x1am;m\x1am;m;m;u;m[u;u[u;u{}[u{}[u{}{}{}\x18\x85\x8aB\xa2\x10\x00\x00\x00\x00\x82\x08k2:u\x9b\x85\xbb\x8d\xbb\x8d\x96l\xc3\x10\x00\x00\x82\x08z\x85\xf6|\xc8)\x00\x00\x00\x00%\x19\x96l%\x19\xcdJ\xfc\x95\xdb\x95f)\x8aB\xfc\x95\x1c\x9e\x1c\x9e\x1c\x9e\xd1k%\x19\xf6|<\xa6\x1c\x9er\x8c%\x19\x00\x00\x00\x00f)\xd5\x84\xcdJf);\xae\\\xae\xd5\x84%\x19\x00\x00\x00\x00\xc8)\x96l%\x19\xd1k}\xb6\x99\x9d%\x19NS}\xb6}\xb6\xbd\xbe}\xb6\xbc\xb6NS\xa2\x10\x00\x00A\x08\x8aB\x96\xa5%\x19\xd1k\xef\xbd\xbe\xdd\xc6\x01\x80y\xdc\xbe\xbd\xbe\xdc\xbe\xbd\xbe\xbd\xbe\xbd\xbe\xbd\xbe\xbd\xbe\xbd\xbe\x9d\xb6\xbd\xbe\x9d\xb6\xbd\xbe}\xb6\x9c\xbe}\xb6}\xb6}\xb6}\xb6}\xb6}\xb6]\xae}\xb6]\xae}\xb6\\\xae]\xae<\xae]\xae<\xae\\\xae<\xae\\\xae<\xa6<\xae<\xa6<\xa6<\xa6<\xa6\x1c\x9e<\xa6\x1c\x9e\x1c\x9e\x1c\x9e\x1c\x9e\x1c\x9e\x1c\x9e\xfc\x95\x1c\x9e\xfc\x95\x1c\x9e\xfc\x95\xfc\x95\xdb\x95\xfc\x95\xdc\x8d\xfc\x95\xdc\x8d\xdb\x95\xdc\x8d\xdc\x8d\xbb\x8d\xbb\x8d\xbb\x8d\xbb\x8d\x9b\x85\xbb\x8d\x9b\x85\x9b\x85\x9b\x85\x9b\x85\x9b\x85\x9b\x85{}\x9b\x85{}{}{}{}[u{}[u{}[u[u;uZu;m;u;m;m;m;m\x1be;m\x1be\x1am\x1ae\x1ae\x1ae\x1ae\xfa\\\x1ae\xfa\\\xfa\\\xfa\\\xfa\\\xdaT\xfa\\\xdaT\xdaT\xdaL\xdaT\xdaL\xdaL\xdaD\xdaL\xb9D\xdaD\xb9D\xdaD\x99<\xb9D\x99<\xb9D\x99<\xb9D\x99<\x99<y<\xb9Dy<\x99<VD\x99<X<y<X<y<X<X<8<X<8<X<748<8<8<\x1748<\x174\x174\x0b\x80\xc6R"\xb3\x12\x92\n\xb3\x12\x92\n\xdb\x95\x99\x9d\xdb\x95\x99\x9d\x18\x85\xb3\x12\xd4\x1a\xb3\x12\xd4\x1a:}\xff\xff\xff\xff\x18\x85\xd4\x1a\x18\x85\xff\xff\xff\xffW\\\x14\x1b\xd9d\xff\xff\xff\xffxT\x14#xT\xbf\xf7\xff\xff\xda\xa55#\x14#U#5#U#U#U#U#u+U#u+u+u+u+\x96+u+\x96+v+\x96+\x96+\x96+\x96+\x96+\x96+\xb63\xb63\xb73\xb63\xb63\xb63\xd73\xb63\xd73\xd73\xd73\x95;\xf7;\xd73\xf7;\xf7;\xf7;\xf7;\xf8;\xf7;\xf8;\xf7;8<\xf7;8<\xf8;9<\xf8;9<9<9<9<9<9<y<9<y<9<yD9<yDyDyDyDyDyD\x9aDyD\x9aDzD\x9aDzD\x9aD\x9aD\xbaL\xb9D\xbaL\xbaL\xdaT\xbaL\xdaT\xb9T\xdaT\xb9T\xdaT\xdaT\xfa\\\xd9d\xfa\\\xfa\\\xfa\\\xd9d\x1ae\x1ae\x1be\x1ae\x1be\x1be\x1am\x1be;m\x1am;m;m;u;u;u;u[u[u{};uZ}Z}{}Z}W\\\x00\x00%\x19k2\xf0B\xc8)\x00\x00%\x19:}\x9b\x85\xbb\x8d%\x19\x00\x00\xcdJ\x91S\x18\x85%\x19\x00\x00\x8aB\x91S\xc8)A\x08\x00\x00\xc8)\xfc\x95z\x85A\x08%\x19\xda\xa5\xfc\x95\x1c\x9e\xfc\x95NS\x00\x00\x96l\x1c\x9er\x8c\x00\x00A\x08\xcdJ\xd1kk2\x82\x08A\x08\x82\x08<\xae\xda\xa5\x82\x08\x00\x00\xcdrRt\xc8)A\x08\x00\x00NS;\xae\x99\x9d\x00\x00\x8aB}\xb6}\xb6}\xb6}\xb6\xcdJ\x00\x00%\x19\xd1k\xd1kf)\xc3\x10\x00\x00\xcdJ\xbd\xbe\xbd\xbe\xbd\xbe\x9c\xc6\xbd\xbe2\x80\x88\x9c\xbe\xdd\xc6\xbd\xbe\xdd\xc6\xbd\xbe\xbd\xbe\xbd\xbe\xdc\xbe\x9c\xbe\xbd\xbe\xbd\xbe\xbd\xbe\x9c\xbe\xbd\xbe\x9c\xbe\xbd\xbe\x9c\xbe\xbd\xbe}\xb6\x9c\xbe}\xb6\x9d\xb6}\xb6}\xb6}\xb6}\xb6}\xb6}\xb6;\xae}\xb6\\\xae}\xb6;\xae]\xae<\xae]\xae<\xae\\\xae<\xae<\xae<\xa6<\xae<\xa6<\xa6<\xa6<\xa6\x1c\x9e<\xa6\x1c\x9e\x1c\x9e\x1c\x9e\x1c\x9e\xfc\x95\x1c\x9e\xfc\x95\x1c\x9e\xdb\x95\xfc\x95\xfc\x95\xfc\x95\xdb\x95\xfc\x95\xdc\x8d\xfc\x95\xdc\x8d\xdc\x8d\xdc\x8d\xdc\x8d\xbb\x8d\xbb\x8d\xbb\x8d\xbb\x8d\x9b\x85\xbb\x8d\x9b\x85\x9b\x85\x9b\x85\x9b\x85\x9b}\x9b\x85{}\x9b}{}{}Z}{}[u{}Zu[u[u[u;u;u;u;u\x1am;m\x1am;m\x1be\x1am\x1be\x1am\x1ae\x1ae\x1ae\x1ae\xfa\\\xfa\\\xfa\\\xfa\\\xb8\\\xfa\\\xdaT\xfa\\\xb9T\xdaT\xb9T\xdaT\xb9T\xdaL\xbaL\xdaL\xb9D\xbaL\xb9D\xb9D\x99<\x9aD\x99<\xb9D\x99<\x99<yD\x99<y<\x99<y<\x99<X<y<X<y<X<X<X<X<8<X<8<X<748<748<\x174\x174\x174\x174\xf7;\x174\xfb\x01\xf4\x00\x91\x00\x00\x00\x00\x00\x00\x00'
	width = 417
	height = 8
	bitsPerPixel = 16
	isCompress = True
	data = compressed_data
	image = rectconvert(width, height, bitsPerPixel, isCompress, data)