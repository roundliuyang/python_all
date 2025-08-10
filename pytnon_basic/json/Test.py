import json


def demo_json_loads():
    """
    演示 json.loads 的使用
    json.loads 用于解码 JSON 数据，将 JSON 字符串转换为 Python 对象
    """
    # JSON 字符串（注意键需要使用双引号）
    json_data = '{"a":1,"b":2,"c":3,"d":4,"e":5}'

    # 使用 json.loads 将 JSON 字符串解析为 Python 字典
    parsed_data = json.loads(json_data)
    print("解析后的数据:", parsed_data)
    print("数据类型:", type(parsed_data))
    print("访问元素 a:", parsed_data['a'])
    print()


def demo_json_dumps():
    """
    演示 json.dumps 的使用
    json.dumps 用于编码 Python 对象，将其转换为 JSON 字符串
    """
    # Python 字典数据
    data = {'a': 'Runoob', 'b': 7}

    # 使用 json.dumps 将 Python 对象转换为 JSON 字符串
    # sort_keys=True 按键排序
    # indent=4 格式化输出，缩进4个空格
    # separators=(',', ': ') 自定义分隔符
    json_string = json.dumps(data, sort_keys=True, indent=4, separators=(',', ': '))
    print("转换后的JSON字符串:")
    print(json_string)
    print("数据类型:", type(json_string))
    print()


def demo_list_json():
    """
    演示处理列表类型的JSON数据
    """
    # 包含字典的列表
    data = [{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}]

    # 转换为JSON字符串
    json_string = json.dumps(data)
    print("列表转JSON:", json_string)

    # 再转换回Python对象
    parsed_data = json.loads(json_string)
    print("JSON转回Python对象:", parsed_data)
    print("第一个元素的a值:", parsed_data[0]['a'])
    print()


def main():
    print("=== JSON loads 示例 ===")
    demo_json_loads()

    print("=== JSON dumps 示例 ===")
    demo_json_dumps()

    print("=== 列表JSON处理示例 ===")
    demo_list_json()


if __name__ == "__main__":
    main()
