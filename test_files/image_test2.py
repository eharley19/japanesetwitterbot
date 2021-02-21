from PIL import Image, ImageDraw, ImageFont

image = Image.open('background2.png')

draw = ImageDraw.Draw(image)



font, font2 = ImageFont.truetype('UDDigiKyokashoN-B.ttc', size=72), ImageFont.truetype('UDDigiKyokashoN-B.ttc', 128)


(x, y) = (100, 50)

message = "今日の単語は"
black_color = "rgb(1, 0, 0)" 



draw.text((x,y), message, fill=black_color, font=font)

(x2, y2) = (550, 200)
kanji = "光"


color = "rgb(252, 255, 46)" 
draw.text((x2, y2), kanji, fill=color, font=font2)



image.save('test_image.png')

