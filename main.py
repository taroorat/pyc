import time
import requests
import json
from numba import jit
import cv2 
import math

@jit
def run():
    p = 0
    for i in range(w):
        for j in range(h):
            for k in range(l):
                p = p+i+j-k
    print(p)

def go_run():
    client = requests.session()
    headers = {'Content-Type': 'application/json', 'Connection': 'keep-alive'}

    response = client.post(url='http://127.0.0.1:31173/cimg', 
                            headers=headers,
                            data=json.dumps(cImg))
    print(response.text)
    client.close()


if __name__ == "__main__":
    w = 1080
    h = 1920
    l = 10

    cImg ={
        "Width":w,
        "Height":h,
        "Length":l
    }

    start_time = time.time()
    run()
    end_time = time.time()
    print("python",end_time - start_time)

    start_time1 = time.time()
    go_run()
    end_time1 = time.time()
    print("go",end_time1 - start_time1)