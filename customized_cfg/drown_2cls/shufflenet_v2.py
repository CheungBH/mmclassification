_base_ = [
    '../../configs/_base_/models/2cls/shufflenet_v2.py',
    '../../configs/_base_/datasets/drown_2cls.py',
    '../../configs/_base_/schedules/imagenet_bs1024_linearlr_bn_nowd.py',
    '../../configs/_base_/default_runtime.py'
]
