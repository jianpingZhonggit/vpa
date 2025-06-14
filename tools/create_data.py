# Copyright (c) OpenMMLab. All rights reserved.
import argparse
import os.path as osp

from data_converter import nuscenes_converter
from data_converter.create_gt_database import create_groundtruth_database


def nuscenes_data_prep(root_path,
                       info_prefix,
                       version,
                       dataset_name,
                       out_dir,
                       max_sweeps=10):
    """Prepare data related to nuScenes dataset.

    Related data consists of '.pkl' files recording basic infos,
    2D annotations and groundtruth database.

    Args:
        root_path (str): Path of dataset root.
        info_prefix (str): The prefix of info filenames.
        version (str): Dataset version.
        dataset_name (str): The dataset class name.
        out_dir (str): Output directory of the groundtruth database info.
        max_sweeps (int, optional): Number of input consecutive frames.
            Default: 10
    """
    # """
    # nuscenes_converter.create_nuscenes_infos(
    #     root_path, info_prefix, version=version, max_sweeps=max_sweeps)

    # if version == 'v1.0-test':
    #     info_test_path = osp.join(root_path, f'{info_prefix}_infos_test.pkl')
    #     nuscenes_converter.export_2d_annotation(
    #         root_path, info_test_path, version=version)
    #     return
    # info_train_path = osp.join(root_path, f'{info_prefix}_infos_train.pkl')
    # info_val_path = osp.join(root_path, f'{info_prefix}_infos_val.pkl')
    # nuscenes_converter.export_2d_annotation(
    #     root_path, info_train_path, version=version)
    # nuscenes_converter.export_2d_annotation(
    #     root_path, info_val_path, version=version)
    # """
    create_groundtruth_database(dataset_name, root_path, info_prefix,
                                f'{out_dir}/nuscenes_vpa_infos_trainval.pkl')


parser = argparse.ArgumentParser(description='Data converter arg parser')
parser.add_argument('dataset', metavar='kitti', help='name of the dataset')
parser.add_argument(
    '--root-path',
    type=str,
    default='./data/kitti',
    help='specify the root path of dataset')
parser.add_argument(
    '--version',
    type=str,
    default='v1.0',
    required=False,
    help='specify the dataset version, no need for kitti')
parser.add_argument(
    '--max-sweeps',
    type=int,
    default=10,
    required=False,
    help='specify sweeps of lidar per example')
parser.add_argument(
    '--with-plane',
    action='store_true',
    help='Whether to use plane information for kitti.')
parser.add_argument(
    '--num-points',
    type=int,
    default=-1,
    help='Number of points to sample for indoor datasets.')
parser.add_argument(
    '--out-dir',
    type=str,
    default='./data/kitti',
    required=False,
    help='name of info pkl')
parser.add_argument('--extra-tag', type=str, default='kitti')
parser.add_argument(
    '--workers', type=int, default=4, help='number of threads to be used')
args = parser.parse_args()


if __name__ == '__main__':
    import importlib
    importlib.import_module('projects.mmdet3d_plugin')

    if args.dataset == 'nuscenes' and args.version != 'v1.0-mini':
        train_version = f'{args.version}-trainval'
        nuscenes_data_prep(
            root_path=args.root_path,
            info_prefix=args.extra_tag,
            version=train_version,
            dataset_name='CustomNuScenesDataset',
            out_dir=args.out_dir,
            max_sweeps=args.max_sweeps)
        test_version = f'{args.version}-test'
        nuscenes_data_prep(
            root_path=args.root_path,
            info_prefix=args.extra_tag,
            version=test_version,
            dataset_name='CustomNuScenesDataset',
            out_dir=args.out_dir,
            max_sweeps=args.max_sweeps)
    elif args.dataset == 'nuscenes' and args.version == 'v1.0-mini':
        train_version = f'{args.version}'
        nuscenes_data_prep(
            root_path=args.root_path,
            info_prefix=args.extra_tag,
            version=train_version,
            dataset_name='CustomNuScenesDataset',
            out_dir=args.out_dir,
            max_sweeps=args.max_sweeps)
