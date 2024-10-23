import os
from tqdm import tqdm
import requests

def download_file(url, local_filename=None, token = None):
    if(local_filename is None):
        local_filename = url.split('/')[-1]
        
    os.makedirs(os.path.dirname(local_filename),exist_ok=True)
        
    print(f"Downloading {url} in {local_filename}")
    
    headers=None
    if(token is not None):
        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/x-binary",
        }

    with requests.get(url, stream=True,headers=headers) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in tqdm(r.iter_content(chunk_size=8192)): 
                # If you have chunk encoded response uncomment if
                # and set chunk_size parameter to None.
                #if chunk: 
                f.write(chunk)
    return local_filename

class DownloadFile:
    @classmethod
    def INPUT_TYPES(s):
        demoCode = '# Input is an array\nprint(len(input))\n#output is a dictionary\nout=dict(test=0)'
        return {"required": {
                                "url": ("STRING", {"multiline":True, "dynamicPrompts": False, "placeholder": "https://civitai.com/api/download/models/928455?type=Model&format=SafeTensor"}),
                                "download_path": ("STRING", {"multiline":False, "dynamicPrompts": False, "placeholder": "./models/lora/test.safetensors"}),
                                "token": ("STRING", {"multiline":False, "dynamicPrompts": False, "placeholder": ""})
                            }
                }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("filename",)
    FUNCTION = "execute"

    CATEGORY = "BilboX/utils"
    OUTPUT_NODE = True
    DYNAMIC_INPUT_NODES=True

    def execute(self, url, download_path, token, **kwargs):
        ret = download_file(url, download_path, None if token=="" else token)
        return (ret,)

    @classmethod
    def IS_CHANGED(s, code, **kwargs):
        return float("NaN")

NODE_CLASS_MAPPINGS = {
    "DownloadFile": DownloadFile
}
