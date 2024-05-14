import cv2
from PIL import ImageFont, ImageDraw, Image
import numpy as np
import random
import os

def fit_text_in_box(font, bounding_box, text):
    x, y, w, h = bounding_box
    best_font_size = 1
    best_num_lines = float('inf')
    best_text_lines = []
    vertical_offset = 0
    for font_size in range(1, h):
        current_font = ImageFont.truetype(font, font_size)
        draw = ImageDraw.Draw(Image.new('RGB', (1, 1)))
        text_width, text_height = draw.textbbox((0, 0), text, font=current_font)[2:]
        lines = []
        line = ''
        for word in text.split():
            if draw.textbbox((0, 0), line + word, font=current_font)[2] <= w:
                line += word + ' '
            else:
                lines.append(line.strip())
                line = word + ' '
        if line:
            lines.append(line.strip())
        num_lines = len(lines)
        total_text_height = text_height * num_lines
        if total_text_height <= h and (num_lines < best_num_lines or (num_lines == best_num_lines and font_size > best_font_size)):
            best_font_size = font_size
            best_num_lines = num_lines
            best_text_lines = lines
            vertical_offset = (h - total_text_height) // 2
    return best_font_size, best_text_lines, vertical_offset

def create_watermark_from_text(text, font_path, image_width, image_height):
    pil_img = Image.new('RGB', (image_width, image_height), (0, 0, 0))
    draw = ImageDraw.Draw(pil_img)
    font_size, lines, vertical_offset = fit_text_in_box(font_path, (0, 0, image_width, image_height), text)
    font = ImageFont.truetype(font_path, font_size)
    y = vertical_offset
    for line in lines:
        text_width, text_height = draw.textbbox((0, 0), line, font=font)[2:]
        x = (image_width - text_width) // 2
        draw.text((x, y), line, font=font, fill=(255, 255, 255))
        y += text_height
    return pil_img

def insert_text_pass(img, watermark):
    return img

def insert_text_simple(img, watermark):
    cv_img = np.array(watermark)
    cv_img = cv2.cvtColor(cv_img, cv2.COLOR_RGB2BGR)
    mask = cv2.cvtColor(cv_img, cv2.COLOR_BGR2GRAY)
    mask = cv2.bitwise_not(mask)
    mask = cv2.merge([mask, mask, mask])
    img = cv2.bitwise_and(img, mask)
    img = cv2.add(img, cv_img)
    return img

if __name__ == '__main__':
    font = os.path.join('fonts', random.choice(os.listdir('fonts')))
    img = cv2.imread('example.jpg')
    watermark = create_watermark_from_text('Lorem ipsum', font, img.shape[1], img.shape[0])
    img1 = insert_text_pass(img, watermark)
    img2 = insert_text_simple(img, watermark)
    cv2.imshow('insert_text_pass', img1)
    cv2.imshow('insert_text_simple', img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()