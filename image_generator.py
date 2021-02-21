from models import Word, app, db
from PIL import Image, ImageDraw, ImageFont
from Colors import Colors
from visualWord import VisualWord

import random

# Size of the image
dimensions = (720, 720)

# The font we'll be using in our image
font = ImageFont.truetype('fonts/KosugiMaru-Regular.ttf', size=45)

for number in range(0, 100):
    random_number = random.randrange(0, db.session.query(Word).count())
    random_word = db.session.query(Word)[random_number]

    output_image = Image.new(
        'RGB', 
        dimensions, 
        Colors.white
    )

    if random_word.kanji:
        header = VisualWord(random_word.kanji, (40, 50), font, Colors.black)
        sub_header = VisualWord(random_word.kana, (40, 100), font, Colors.black)
        romaji_text = VisualWord(random_word.romaji, (40, 150), font, Colors.black)
        definition_text = VisualWord(random_word.definition, (40, 200), font, Colors.black)

        image_in_memory = ImageDraw.Draw(output_image)

        for visual_word in [header, sub_header, romaji_text, definition_text]:
            image_in_memory.text(
                visual_word.position, 
                visual_word.display_text, 
                fill=visual_word.color, 
                font=visual_word.font, 
                align=visual_word.alignment
            )

        output_image.save(f'images/test_image_{number}.png')