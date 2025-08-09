import json

def main():
    jsonData = '{"a":1,"b":2,"c":3,"d":4,"e":5}'
    # json.loads 用于解码 JSON 数据。该函数返回 Python 字段的数据类型。
    text = json.loads(jsonData)
    print(text)

if __name__ == "__main__":
    main()