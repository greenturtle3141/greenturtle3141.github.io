import imager
 
print 'Load Paintball Map...'
picture = imager.load_image('fixedhero.png')
print 'Loading Rainbow...'
rainbow = imager.load_image('rainbow.png')
 
print 'Creating density array...'
density = [0] * 439
for i in xrange(439):
    density[i] = ([0] * 218)
 
print 'Starting algorithm...'
for rowNum, row in enumerate(picture): #194
    for pixNum, pixel in enumerate(row): #162
        print 'Row: ', rowNum, 'Pixel: ', pixNum
        if picture[rowNum][pixNum] !=  (255, 255, 255):
  
            for rowNumSquare in xrange(rowNum-50, rowNum+50):
                for pixNumSquare in xrange(pixNum-50, pixNum+50):
                    if rowNumSquare<0 or rowNumSquare>=439 or pixNumSquare<0 or pixNumSquare>=218:
                        continue   
                    else:
                        if ((abs(rowNumSquare - rowNum))**2+(abs(pixNumSquare - pixNum))**2)**.5 <= 50:
                            density[rowNumSquare][pixNumSquare] += 1
     
print 'Coloring picture'
           
for rowNum, row in enumerate(picture):
    for pixNum, pixel in enumerate(row):
 
        color = (density[rowNum][pixNum]) * 1019 / 7854
        picture[rowNum][pixNum] = rainbow[0][color]
 
print 'Opening Picture...'       
imager.show_image(picture)
