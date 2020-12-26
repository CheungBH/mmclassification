import os

model_config = {
    "work_dirs/drown_walk-mobile/latest.pth":
        "customized_cfg/drown_2cls/mobilenet_v2.py",
    "work_dirs/drown_walk-shuffle/latest.pth": "customized_cfg/drown_2cls/shufflenet_v2.py"
}

for idx, (model, config) in enumerate(model_config.items()):
    print("---------------------Converting model {}---------------------------".format(idx))
    onnx_path = os.path.join("/".join(model.split("/")[:-1]), "model.onnx")
    onnx_cmd = "python tools/pytorch2onnx.py {} --checkpoint {} --verify --output-file {}".format(config, model, onnx_path)
    print(onnx_cmd)
    os.system(onnx_cmd)
    sim_cmd = "python -m onnxsim {} {}".format(onnx_path, onnx_path.replace("onnx", "_sim.onnx"))
    print(sim_cmd)
    os.system(sim_cmd)


