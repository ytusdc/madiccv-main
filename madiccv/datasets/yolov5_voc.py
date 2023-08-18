# Copyright (c) OpenMMLab. All rights reserved.
from mmdet.datasets import VOCDataset


from ..registry import DATASETS
from madiccv.datasets.yolov5_coco import BatchShapePolicyDataset

@DATASETS.register_module()
class YOLOv5VOCDataset(BatchShapePolicyDataset, VOCDataset):
    """Dataset for YOLOv5 VOC Dataset.

    We only add `BatchShapePolicy` function compared with VOCDataset. See
    `mmyolo/datasets/utils.py#BatchShapePolicy` for details
    """
    pass
