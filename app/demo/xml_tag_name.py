import xml.etree.ElementTree as ET
import json


# 根据名称来获取XML元素及其子元素

def xml_to_dict(element):
    """
    将XML元素及其子元素转换为字典
    """
    # 如果元素没有子元素，则直接返回其文本内容
    if len(element) == 0:
        return element.text

    # 如果有子元素，则递归处理
    result = {}
    for child in element:
        child_data = xml_to_dict(child)
        # 处理同名标签（转换为列表）
        if child.tag in result:
            if not isinstance(result[child.tag], list):
                result[child.tag] = [result[child.tag]]
            result[child.tag].append(child_data)
        else:
            result[child.tag] = child_data

    # 添加属性
    if element.attrib:
        result['@attributes'] = element.attrib

    return result


def filter_by_tag(data, tag_name):
    """
    根据标签名筛选数据
    """
    results = []

    def search_recursive(obj, target_tag):
        if isinstance(obj, dict):
            for key, value in obj.items():
                if key == target_tag:
                    results.append(value)
                elif isinstance(value, (dict, list)):
                    search_recursive(value, target_tag)
        elif isinstance(obj, list):
            for item in obj:
                search_recursive(item, target_tag)

    search_recursive(data, tag_name)
    return results


# def main(tagName):
#     tree = ET.parse('product.xml')
#     root = tree.getroot()
#
#     # 转换整个XML为字典
#     xml_dict = {root.tag: xml_to_dict(root)}
#
#     # 转换为JSON格式
#     json_output = json.dumps(xml_dict, indent=2, ensure_ascii=False)
#     filtered_data = filter_by_tag(xml_dict, tagName)
#     return json.dumps(filtered_data, indent=2, ensure_ascii=False)
#
if __name__ == '__main__':
    tree = ET.parse('product.xml')
    root = tree.getroot()

    # 转换整个XML为字典
    xml_dict = {root.tag: xml_to_dict(root)}

    # 转换为JSON格式
    json_output = json.dumps(xml_dict, indent=2, ensure_ascii=False)

    # 示例：根据标签名筛选数据
    # 假设你想筛选所有 'product' 标签的内容
    tagName = input('输入需要筛选的内容: ')
    filtered_data = filter_by_tag(xml_dict, tagName)
    print(f"筛选结果: {json.dumps(filtered_data, indent=2, ensure_ascii=False)}")

    # 保存完整JSON到文件
    # with open('output.json', 'w', encoding='utf-8') as f:
#     #     f.write(json_output)
