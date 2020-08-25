from PIL import Image, ImageDraw, ImageFont

# Create Image object with the input image

try:
    image = Image.open('background.png')
    print("All done loading!")
except Exception as e:
    print("Something went wrong", e)

# Initialize the drawing context
# The image object as background

draw = ImageDraw.Draw(image)

# Create font object with the font file and specify
# desired size

font = ImageFont.truetype('UDDigiKyokashoN-B.ttc', size=46)

# Tuple that represents the position of the message

(x, y) = (100, 75)

message = "宜しくお願い致します！"
black_color = "rgb(100, 0, 100)" # Black

# draw the image on the background

draw.text((x,y), message, fill=black_color, font=font, align="center")

(x2, y2) = (150, 150)
name = "ケーシーさん"
white_color = "rgb(255, 255, 225)" # White
draw.text((x2, y2), name, fill=white_color, font=font, align="center")

# Save the edited image!

image.save('greeting_card.png')