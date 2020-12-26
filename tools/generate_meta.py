import os

val_root = "../data/CatDog/val"
meta_root = val_root.replace("val", "meta")

os.makedirs(meta_root, exist_ok=True)
with open(os.path.join(meta_root, "val.txt"), "w") as val_txt:
    for idx, sub_folder in enumerate(os.listdir(val_root)):
        for file_name in os.listdir(os.path.join(val_root, sub_folder)):
            val_txt.write(os.path.join(val_root, sub_folder, file_name) + " {}".format(idx) +"\n")
