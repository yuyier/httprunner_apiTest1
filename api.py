from flask import Flask, request
import json

# 创建一个服务，赋值给APP
app = Flask(__name__)


# 指定接口访问的路径，支持什么请求方式get，post
@app.route('/shopee/test', methods=['post', 'get'])
# 请求后直接拼接入参方式
def get_ss():
    # 使用request.args.get方式获取拼接的入参数据
    a = request.args.get('a')
    b = request.args.get('b')
    
    result = {
        'error_code': "0",
        'error_message': "success",
        'reference': "111"
    }
    response = json.dumps(result)
    
# 输出结果
            return response


app.run(host='0.0.0.0', port=8880, debug=True)
