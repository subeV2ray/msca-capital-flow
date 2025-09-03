import xml.etree.ElementTree as ET
import json


def get_tags_with_hierarchy(xml_file):
    """
    获取XML文件中所有标签名及其层级关系

    Args:
        xml_file (str): XML文件路径

    Returns:
        dict: 标签名及其层级关系的字典
    """
    tree = ET.parse(xml_file)
    root = tree.getroot()

    hierarchy = {}

    def build_hierarchy(element, parent_dict, level=0):
        tag = element.tag

        # 如果标签已存在，确保它在当前层级只被处理一次
        if tag not in parent_dict:
            parent_dict[tag] = {}

        # 递归处理子元素
        for child in element:
            build_hierarchy(child, parent_dict[tag], level + 1)

    # 从根元素开始构建层级结构
    hierarchy[root.tag] = {}
    for child in root:
        build_hierarchy(child, hierarchy[root.tag])

    return hierarchy


def get_tags_with_children(xml_file):
    """
    获取每个标签及其直接子标签

    Args:
        xml_file (str): XML文件路径

    Returns:
        dict: 每个标签及其直接子标签的字典
    """
    tree = ET.parse(xml_file)
    root = tree.getroot()

    tag_children = {}

    def collect_children(element):
        tag = element.tag
        children = set()

        # 收集直接子标签
        for child in element:
            children.add(child.tag)

        # 如果标签已存在，合并子标签集合
        if tag in tag_children:
            tag_children[tag].update(children)
        else:
            tag_children[tag] = children

        # 递归处理子元素
        for child in element:
            collect_children(child)

    collect_children(root)

    # 将集合转换为排序列表
    result = {}
    for tag, children in tag_children.items():
        result[tag] = sorted(list(children))

    return result


def save_hierarchy_to_json(hierarchy_dict, output_file):
    """
    将层级关系保存到JSON文件

    Args:
        hierarchy_dict (dict): 层级关系字典
        output_file (str): 输出文件路径
    """
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(hierarchy_dict, f, indent=2, ensure_ascii=False)


def save_hierarchy_as_text(hierarchy_dict, output_file):
    """
    将层级关系保存为文本文件

    Args:
        hierarchy_dict (dict): 层级关系字典
        output_file (str): 输出文件路径
    """

    def write_hierarchy(file_handle, hierarchy, level=0):
        indent = "  " * level
        for tag, children in hierarchy.items():
            file_handle.write(f"{indent}- {tag}\n")
            if children:  # 如果有子标签
                write_hierarchy(file_handle, children, level + 1)

    with open(output_file, 'w', encoding='utf-8') as f:
        write_hierarchy(f, hierarchy_dict)


if __name__ == '__main__':
    xml_file = 'product.xml'

    # 方法1: 获取完整的层级结构
    print("=== 完整层级结构 ===")
    full_hierarchy = get_tags_with_hierarchy(xml_file)
    print(json.dumps(full_hierarchy, indent=2, ensure_ascii=False))

    # 保存完整层级结构到JSON文件
    save_hierarchy_to_json(full_hierarchy, 'tag_hierarchy.json')
    print("\n完整层级结构已保存到 tag_hierarchy.json")

    # 方法2: 获取每个标签的直接子标签
    print("\n=== 每个标签的直接子标签 ===")
    tag_children = get_tags_with_children(xml_file)
    for tag, children in tag_children.items():
        print(f"{tag}: {children}")

    # 保存标签及其子标签到JSON文件
    save_hierarchy_to_json(tag_children, 'tag_children.json')
    print("\n标签及其子标签已保存到 tag_children.json")

    # 保存为文本格式
    save_hierarchy_as_text(full_hierarchy, 'tag_hierarchy.txt')
    print("层级结构已保存到 tag_hierarchy.txt")
