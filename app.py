# 导入所需的模块
from flask import Flask, jsonify, request

# 创建一个Flask应用实例
app = Flask(__name__)


# --- 定义一个自定义的Python类 ---
# 这个类用于将对象序列化为JSON
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 定义一个方法来将对象转换为字典
    def to_dict(self):
        return {
            "name": self.name,
            "age": self.age
        }


# 定义一个路由来处理 /data 的GET请求
# 这个路由用于发送数据给客户端
@app.route('/data', methods=['GET'])
def get_data():
    # 创建 User 类的一个实例
    user_instance = User("Alex", 18)

    # 调用 to_dict() 方法，将对象转换为字典
    user_dict = user_instance.to_dict()

    # 使用 jsonify 将字典转换为JSON响应并返回
    return jsonify(user_dict)


# --- 新增：一个用于接收数据的路由 ---
# 这个路由使用 POST 方法来接收JSON数据
@app.route('/data', methods=['POST'])
def receive_data():
    # 确保请求的 Content-Type 是 application/json
    if not request.is_json:
        return jsonify({"error": "Request must be JSON"}), 400

    # 尝试从请求体中获取 JSON 数据
    try:
        data = request.json
        # 验证 JSON 数据中是否包含 name 和 age
        if "name" not in data or "age" not in data:
            return jsonify({"error": "Missing 'name' or 'age' in JSON data"}), 400

        name = data.get('name')
        age = data.get('age')

        # 在这里，您可以对接收到的数据进行处理，比如保存到数据库
        # 这里我们仅简单地返回一个确认信息
        print(f"Received data: Name: {name}, Age: {age}")
        return jsonify({
            "message": "Data received successfully!",
            "received_data": {
                "name": name,
                "age": age
            }
        }), 200

    except Exception as e:
        # 如果JSON格式不正确，则捕获异常并返回错误
        return jsonify({"error": f"Invalid JSON format: {e}"}), 400


# 确保只有在直接运行此脚本时才启动应用
if __name__ == '__main__':
    # 启动应用，并开启调试模式以便查看错误
    app.run(debug=True)
