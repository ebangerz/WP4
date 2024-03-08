
def store_files(list):
    with open('images.txt', 'w') as file:
        for images in list:
            file.write(images + '\n')

def get_files():
    with open('images.txt', 'r') as file:
        images = file.readlines()
        images = [lines.strip() for lines in images]
    return images