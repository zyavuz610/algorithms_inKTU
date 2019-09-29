from birlestirmelisıralama import Merge
def bot(b):
	size = 1
	while size < len(b):
		size+=size
		for i in range(0, len(b), size):
			ilk = i
			orta   = i + (size / 2)
			son = i + size
			left  = b[ ilk : orta ]
			right = b[   orta : son ]
			b[ilk:son] = Merge.merge(left, right,b)
	print(b)