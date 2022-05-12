# Deep Learning Final Project

## Data
See [data readme](data/README.md)

## Add a new image

Notebook: https://colab.research.google.com/drive/1FtlPRbUT3ipQnKOcq1_sH8d7eZ7_vcwB?authuser=2#scrollTo=Ov3DXqfY2LjJ

1. All images of models (person) should be in `tryon_folder`. When a new person is added, please be sure they have a transparent background and are of PNG. The name should have `_whole_front.png` at the end
2. All outputs from styletransfer images should be in `style_transfer` as a `png` with a transparent background
3. You should update `tryon_folder/test_pairs.txt` with a model -> style_transfer combination you want, for example
```
person_whole_front.png    shirt.jpg
```

## M3D-VTON

This is a copied version of the code available at https://github.com/fyviezhao/M3D-VTON

You need to load the pretrained models from this url (see readme.txt on where to put the models). Unfortunately the models are too big to fit in git https://figshare.com/s/fad809619d2f9ac666fc?file=30740524

Follow the documentation from that project to run inference calls. IE

```bash
python3 M3D-VTON/test.py --model MTM
python3 M3D-VTON/test.py --model DRM
python3 M3D-VTON/test.py --model TFM
python3 M3D-VTON/rgbd2pcd.py
```
By default, this will use data in the parent [data](../data) directory and put results in the parent [results](../results) (see [test_options](test_options.py))

This runs everything:
1. Monocular Prediction Module (MTM?? - inconsistency in paper)
2. Depth Refinement Module (DRM)
3. Texture Fusion Module (TFM)
4. RGB to point cloud

You can then load the results in Meshlab by importing the results from a single file in `results/aligned/pcd/test_pairs/*.ply`.  To make it look better:
* Normal Estimation: Open MeshLab and load the point cloud file, and then go to Filters --> Normals, Curvatures and Orientation --> Compute normals for point sets
* Possion Remeshing: Go to Filters --> Remeshing, Simplification and Reconstruction --> Surface Reconstruction: Screen Possion (set reconstruction depth = 9)


## OpenPose
Copied from https://github.com/CMU-Perceptual-Computing-Lab/openpose
See https://maelfabien.github.io/tutorials/open-pose/#installation for installation
