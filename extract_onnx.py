#-*-coding:utf-8-*-
import os

root_path = "work_dirs"
onnx_path = "onnx"
os.makedirs(onnx_path, exist_ok=True)

dirs = [f for f in os.listdir(root_path)]
model_paths = []

for dir in dirs:
    model_path = os.path.join(root_path, dir, "model_sim.onnx")
    dest_path = os.path.join(onnx_path, dir + ".onnx")
    if os.path.exists(model_path) and not os.path.exists(dest_path):
        cmd = "cp {} {}".format(model_path, dest_path)
        print(cmd)
        os.system(cmd)
