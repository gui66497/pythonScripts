#!/usr/bin/env python
# -*- coding: utf-8 -*-
# by fgt 2018/11/14
from flask import Flask, abort, request, jsonify

app = Flask(__name__)

# 测试数据暂时存放
tasks = []

# 新增
@app.route('/add_task/', methods=['POST'])
def add_task():
    if not request.json or 'id' not in request.json or 'info' not in request.json:
        abort(400)
    task = {
        'id': request.json['id'],
        'info': request.json['info']
    }
    tasks.append(task)
    return jsonify({'result': 'success'})

# 查询
@app.route('/get_task/', methods=['GET'])
def get_task():
    if not request.args or 'id' not in request.args:
        # 没有指定id则返回全部
        return jsonify(tasks)
    else:
        task_id = request.args['id']
        task = filter(lambda t: t['id'] == int(task_id), tasks)
        return jsonify(task) if task else jsonify({'result': 'not found'})

# 删除
@app.route('/del_task/', methods=['DELETE'])
def del_task():
    global tasks
    if not request.args or 'id' not in request.args:
        # 没有指定id
        return jsonify({'result': 'no id'})
    else:
        task_id = request.args['id']
        tasks = filter(lambda t: t['id'] != int(task_id), tasks)
        # tasks = task
        return jsonify({'result':"success"}) 

# 启动
if __name__ == "__main__":
    # 将host设置为0.0.0.0，则外网用户也可以访问到这个服务
    app.run(host="0.0.0.0", port=8383, debug=True)