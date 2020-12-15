import time
import requests
import json
from numba import jit
import cv2 
import math

def go_run():
    client = requests.session()
    headers = {'Content-Type': 'application/json', 'Connection': 'keep-alive'}

    response = client.post(url='http://127.0.0.1:31173/img2Domino/shapeCone3d', 
                            headers=headers,
                            data=json.dumps(src_img_info))
    print(response.text)
    client.close()


if __name__ == "__main__":

    img_name = "./images/pikachu001.jpg"
    common_bgr_color = [{"color":"green",
                        "bgr":[0,255,0]},
                        {"color":"yellow",
                        "bgr":[255,0,0]},
                        {"color":"red",
                        "bgr":[0,0,255]}]
    src_img_info ={
        "img_name": img_name,
        "common_bgr_color": common_bgr_color,
    }

    start_time = time.time()
    go_run()
    print(json.dumps(src_img_info))
    end_time = time.time()
    print("go",end_time - start_time)