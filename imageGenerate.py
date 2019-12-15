from io import BytesIO
from flask import  make_response
from PIL import Image, ImageDraw, Image, ImageFont

class CardBusiness():

    def __init__(self, data):
        self.data = data

    def final_card(self):
        self.base = Image.open('src/Front-2.png').convert('RGBA')

        # Creating a blank image for the text, initialized to transparent text color
        self.txt = Image.new('RGBA', self.base.size, (255, 255, 255, 0))

        # Getting the font using both the size and font path already setted
        self.font = ImageFont.truetype('fonts/AvertaBlack.otf', 80)
        self.font2 = ImageFont.truetype('fonts/Averta.otf', 40)

        # Getting a drawing context on the 'txt' blank image
        self.d = ImageDraw.Draw(self.txt)


        # Drawing the text with the coordinate and name inputs
        self.d.text((450, 100), self.data["Nome"], font=self.font,
                    fill=(0, 91, 170, 255))

        # Joining both images in one

        self.d.text((450, 190), self.data["Sobrenome"], font = self.font, fill=(0, 91, 170, 255))


        self.d.text((450, 300), self.data["Cargo"], font = self.font2, fill= (10, 10, 10, 255))

        self.out = Image.alpha_composite(self.base, self.txt)

        return self.out


class ReturnImage():
    def __init__(self, img):
        self.img= img

    def generate_response(self):
        img_bytes = BytesIO()
        self.img.save(img_bytes, format="PNG", quality=95)
        self.img = img_bytes.getvalue()
        response = make_response(self.img)
        response.content_type = "image/png"
        length = len(self.img)
        response.content_length = length
        return response

