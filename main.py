import time
import requests
import json

def go_run():
    client = requests.session()
    headers = {'Content-Type': 'application/json', 'Connection': 'keep-alive'}

    response = client.post(url='http://127.0.0.1:31173/img2Domino/shapeCone3d', 
                            headers=headers,
                            data=json.dumps(src_img_info))
    print(response.text)
    client.close()


if __name__ == "__main__":

    img_name = "d:/GoPath/src/taro.117/gospyc/images/pikachu001.jpg"
    common_bgr_color = [
                            {"color":"green",
                            "bgr":[0,255,0]},
                            {"color":"yellow",
                            "bgr":[0, 255, 255]},
                            {"color":"red",
                            "bgr":[0,0,255]},
                            {"color":"blue",
                            "bgr":[255, 0, 0]},
                            {"color":"orange",
                            "bgr":[0, 165, 255]},
                        ]

    src_img_info = {
        "img_name": img_name,
        "common_bgr_color": common_bgr_color,
    }

    start_time = time.time()
    go_run()
    # print(json.dumps(src_img_info))
    end_time = time.time()
    print("go",end_time - start_time)