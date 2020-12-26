import os

work_dirs = "--work-dir work_dirs/cat_dog"

configs = {
    "customized_cfg/CatDog/mobilenet_v2.py": "mobile",
    "customized_cfg/CatDog/resnet18.py": "resnet18",
    "customized_cfg/CatDog/resnet34.py": "resnet34",
    "customized_cfg/CatDog/resnetv1d50.py": "resnetv1d50",
    "customized_cfg/CatDog/resnext50.py": "resnext50",
    "customized_cfg/CatDog/seresnet50.py": "seresnet50",
    "customized_cfg/CatDog/shufflenet_v2.py": "shuffle",
}

cmds = []

for config, out_name in configs.items():
    cmds.append("python tools/train.py {} {}-{}".format(config, work_dirs, out_name))

for idx, cmd in enumerate(cmds):
    print("----------------------------------Training model {}-----------------------------------".format(idx))
    print(cmd)
    os.system(cmd)
