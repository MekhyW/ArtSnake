from PIL import ImageFont, ImageDraw, Image

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

def insert_text_pass(img):
    return img

if __name__ == '__main__':
    import cv2
    img = cv2.imread('image1.jpg')
    img = insert_text_pass(img)
    cv2.imshow('image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()