import exifread

def get_image_creation_date(image_path):
    with open(image_path, 'rb') as image_file:
        tags = exifread.process_file(image_file)
        if 'EXIF DateTimeOriginal' in tags:
            return str(tags['EXIF DateTimeOriginal'])
        else:
            return None

image_path = 'messi.jpg'
creation_date = get_image_creation_date(image_path)
if creation_date:
    print(f"Image creation date: {creation_date}")
else:
    print("Creation date not found in EXIF data.")
import exifread

def get_all_exif_tags(image_path):
    with open(image_path, 'rb') as image_file:
        tags = exifread.process_file(image_file)
        return tags

image_path = 'messi.jpg'
exif_tags = get_all_exif_tags(image_path)
print(exif_tags)
# from PIL import Image
# from PIL.ExifTags import TAGS
#
# # open the image
# image = Image.open("messi.jpg")
#
# # extracting the exif metadata
# exifdata = image.getexif()
#
# # looping through all the tags present in exifdata
# for tagid in exifdata:
#     # getting the tag name instead of tag id
#     tagname = TAGS.get(tagid, tagid)
#     # passing the tagid to get its respective value
#     value = exifdata.get(tagid)
#     # printing the final result
#     print(f"{tagname:25}: {value}")
