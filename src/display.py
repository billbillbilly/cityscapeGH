from PIL import Image
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('--work_dir', 
                    type=str, 
                    default='', 
                    help='where to open images')
parser.add_argument('--type', 
                    type=str, 
                    default='label', 
                    help='label or scene')
args = parser.parse_args()

os.chdir(args.work_dir)

img = Image.open('temp/label_img.jpg') if args.type == 'label' else Image.open('temp/scene.jpg')
if args.type == 'label':
    images = [Image.open(x) for x in ['temp/label_img.jpg', 'temp/label_img.jpg']]
    widths, heights = zip(*(i.size for i in images))
    total_width = sum(widths)
    max_height = max(heights)
    new_im = Image.new('RGB', (total_width, max_height))
    x_offset = 0
    for im in images:
        new_im.paste(im, (x_offset,0))
        x_offset += im.size[0]
    new_im.save('src/pix2pix_model/imgs/test/label_img.jpg')

#img.show()