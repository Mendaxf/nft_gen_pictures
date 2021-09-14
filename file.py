from PIL import Image
import glob
import random
#part folders 
fon 	= 	glob.glob('fon/*.png')
obj 	= 	glob.glob('object/*.png')
hair 	= 	glob.glob('hair/*.png')
clothes = 	glob.glob('clot/*.png')

def gen_image(i):
	for i in range(i):
		imbg = Image.open(random.choice(fon))
		s = [obj, hair, clothes]
		for x in s:
			print(x)
			if not x:
				continue
			imfg = Image.open(random.choice(x))
			imfg_resized = imfg.resize(imbg.size, Image.LANCZOS)
			imbg.paste(imfg_resized, None, imfg_resized)		
			continue
		imbg.save(str(i)+".png")