import base64
import json
import io
import json

def file_to_code(file_path):
    with open(file_path, "rb") as file:
        file_data = file.read()
        encoded_data = base64.b64encode(file_data).decode('utf-8')
        return encoded_data
    
def code_to_file(code, name):
    ppt_binary = base64.b64decode(code)
    # 將二進制內容寫入 PPT 文件
    with open(name, "wb") as file:
        file.write(ppt_binary)