# Copyright (c) OpenMMLab. All rights reserved.
from .yolov5_head import YOLOv5Head, YOLOv5HeadModule
from .yolov8_head import YOLOv8Head, YOLOv8HeadModule
from .yolox_head import YOLOXHead, YOLOXHeadModule

__all__ = [
    'YOLOv5Head',  'YOLOXHead', 'YOLOv5HeadModule',
     'YOLOXHeadModule','YOLOv8Head', 'YOLOv8HeadModule',
]
