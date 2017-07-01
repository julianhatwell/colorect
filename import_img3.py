# from PIL import Image
# img = Image.open('image.tif')
# img.save('image.jpg')
# Colorectal Cancer Histology Tissue Images Parameters
images_path = "\image_tiles_5000" # relative path

# routine to get image file paths and class labels
num_files_in_path = []
filenames = []
filefullpaths = []

for root, dirs, files in os.walk(os.getcwd() + images_path, topdown=False):
    if images_path in dirs:
        dirs.remove(images_path)
    if dirs:
        classes = dirs
    nfiles = 0
    for name in files:
        if os.path.splitext(os.path.join(root, name))[1].lower() == ".jpg":
            nfiles += 1
            filenames.append(name)
            filefullpaths.append(os.path.join(root, name))
    if not dirs:
        num_files_in_path.append(nfiles)

num_images = len(filenames) # 5000
num_classes = len(classes) # 8

#     for name in files:
#         if os.path.splitext(os.path.join(root, name))[1].lower() == ".tif":
#             print(os.path.join(root))
#             if os.path.isfile(os.path.splitext(os.path.join(root, name))[0] + ".jpg"):
#                 print("A jpeg file already exists for %s" % name)
#             # If a jpeg is *NOT* present, create one from the tiff.
#             else:
#                 outfile = os.path.splitext(os.path.join(root, name))[0] + ".jpg"
#                 print(outfile)
#                 try:
#                     im = Image.open(os.path.join(root, name))
#                     print("Generating jpeg for %s" % name)
#                     im.thumbnail(im.size)
#                     im.save(outfile, "JPEG", quality=100)
#                 except:
#                     print("Unexpected Error:", sys.exc_info()[0])
#                     raise
