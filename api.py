import requests
import random
import fileio


#URL: https://ronreiter-meme-generator.p.rapidapi.com/meme


import requests

def get_list_images():
    url = "https://ronreiter-meme-generator.p.rapidapi.com/images"

    headers = {
        "X-RapidAPI-Key": "0d87bb282amsha22fee2d01f762dp158e60jsnb3f0eba56dd2",
        "X-RapidAPI-Host": "ronreiter-meme-generator.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)
    images = response.json()
    fileio.store_files(images)
    response.close()

def return_info(top_text, bottom_text):
    get_list_images()
    
    image_list = fileio.get_files()
    rand_meme = random.choice(image_list)

    url = "https://ronreiter-meme-generator.p.rapidapi.com/meme"

    querystring = {"top": top_text, "bottom": bottom_text, "meme": rand_meme,"font_size":"50","font":"Impact"}

    headers = {
        "X-RapidAPI-Key": "0d87bb282amsha22fee2d01f762dp158e60jsnb3f0eba56dd2",
        "X-RapidAPI-Host": "ronreiter-meme-generator.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    return response
