
import os

model_config = {
    "work_dirs/drown_walk-mobile/latest.pth":
        "customized_cfg/drown_2cls/mobilenet_v2.py",
    "work_dirs/drown_walk-shuffle/latest.pth": "customized_cfg/drown_2cls/shufflenet_v2.py"
}

cmds = []

for model, config in model_config.items():
    dest_folder = os.path.join("/".join(model.split("/")[:-1]), "vis_img")
    os.makedirs(dest_folder, exist_ok=True)
    cmd = "python tools/test.py {} {} --out {} ".format(config, model, dest_folder)
    cmds.append(cmd)
    # model_name = model.replace("work_dirs/", "").replace("/", "-")[:-4]
    # for img_name in os.listdir(img_path):
    #     os.system(cmd)
    #     print(cmd)

for idx, cmd in enumerate(cmds):
    print("----------------------------------Visualizing model {}-----------------------------------".format(idx))
    print(cmd)
    os.system(cmd)
