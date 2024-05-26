import requests
from pydub import AudioSegment
import io
from helper import transform_string,append_to_json_file,read_file
from settings import * 
from bs4 import BeautifulSoup
import random 

def extract_information(tag,extracting_way):
    if extracting_way == 0:
        return tag.text
    if extracting_way == 1:
        return tag["data-audiosource"]
    return None

def scrapper(soup,scrapper_info):
    temp = {} 
    for d in scrapper_info:
        elm = soup
        path_len = len(d["path"]) - 1
        for index,info in enumerate(d["path"]):
            elm = elm.find(info["tag"],**info["attributes"])
            if path_len == index:
                exin = extract_information(elm,d["extract"])
                if d["name"] == "title":
                    exin = exin.replace("\n","").split(":")[0]
                if d["name"] == "author":
                    pass
                temp[d["name"]] = exin
            
    temp["audio"] = extract_audio(temp["audio"],temp["title"])
    return temp 

def extract_audio(audio_url,file_name):
    response = requests.get(audio_url)
    transform_file_name = transform_string(file_name)
    path = f"./audio/{transform_file_name}.mp3"

    if response.status_code == 200:
        audio_data = io.BytesIO(response.content)

        audio = AudioSegment.from_file(audio_data, format="mp3")

        audio.export(path, format="mp3")
        print(f"Audio {file_name} downloaded successfully.")
        return path
    else:
        print(f"There was an error downloading the audio {file_name}.")
        return None

def send_request(link,path):
    UAS = read_file(path)
    user_agent = UAS[random.randrange(len(UAS))].replace("\n","")
    headers = {"user-agent": user_agent}
    return requests.get(link, headers=headers)
