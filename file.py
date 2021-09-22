from PIL import Image
import random
# xa = random.uniform(-3,3)
# xb = random.uniform(-5,3)
# ya = random.uniform(-3,3)
# yb = random.uniform(-3,3)
# maxIt = 256 
# imgx = 720
# imgy = 680

# image = Image.new("RGB", (imgx, imgy))
# mtx = image.load()

# lutx = [j * (xb-xa) / (imgx - 1) + xa for j in range(imgx)]

# for y in range(imgy):
#     cy = y * (yb - ya) / (imgy - 1)  + ya
#     for x in range(imgx):
#         c = complex(lutx[x], cy)
#         z = 0
#         for i in range(maxIt):
#             if abs(z) > 2.0: break 
#             z = z * z + c 
#         r = i % 4 * 64
#         g = i % 8 * 32
#         b = i % 16 * 16
#         mtx[x, y] =  r,g,b

# image.save("over.png", "PNG")
w, h, zoom = 700,600,1


bitmap = Image.new("RGB", (w, h), "white")
  
pix = bitmap.load()
     
# -0.7, 0.27015
cX = random.uniform(-1,1)
print(cX)
cY = random.uniform(-0.3,0.3)
print(cY)
# 0.0, 0.0
moveX = random.uniform(-0.5,0.5) 
print(moveX)
moveY = random.uniform(-0.5,0.5)
print(moveY)
maxIter = 255
   
for x in range(w):
    for y in range(h):
		# zx = 1.5*(x - w/2)/(0.5*zoom*w) + moveX
        zx = 1.5*(x - w/2)/(0.5*zoom*w) + moveX
        zy = 1.0*(y - h/2)/(0.5*zoom*h) + moveY
        i = maxIter
        while zx*zx + zy*zy < 4 and i > 1:
            tmp = zx*zx - zy*zy + cX
            zy,zx = 2.0*zx*zy + cY, tmp
            i -= 1
        pix[x,y] = (i << 21) + (i << 10) + i*8
  
bitmap.save("over.png","PNG")