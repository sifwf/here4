import base64
def extract_images(games):
    images=[]
    for game in games:
        images.append(game[4])
    return images

def delete_photo(games):
        
    for i in range(len(games)):
        games[i].pop(4) 
def encode_images(raw_images):
    en_images=[]
    for image in raw_images:
        en_images.append(base64.b64encode(image).decode('utf-8'))
    return en_images