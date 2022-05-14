"""
creates fun gifs from point clouds 

ref:
http://www.open3d.org/docs/0.7.0/tutorial/Advanced/customized_visualization.html

I ran with these dependencies:
    numpy=1.21.4
    open3d=0.15.1
    matplotlib=3.4.3
    imageio=2.13.5

YMMV. open3d is nice but documentation sucks
"""

import glob
import numpy as np
import open3d as o3d
from matplotlib import pyplot as plt
import imageio

# CHANGE ME ---------------------------------------------
FOLDER = "/Users/anna/Git/aspfohl/deeep-learning"
SAMPLE = "Jessica-Walker-Full-Body-Shot--scaled-removebg-preview"
DEPTH = True
# -------------------------------------------------------

f_root = "results/aligned/pcd/test_pairs"
f = f"{FOLDER}/{f_root}/{SAMPLE}.ply"
o_temp = f"{FOLDER}/temp"

count = 0


def rotate_view(vis):
    global count

    # first thing, make the background black
    opt = vis.get_render_option()
    if opt.background_color.sum() != 0:
        opt.background_color = np.asarray([0, 0, 0])
        return False  # ? if you don't do this, first image will have white bg

    # then, rotate
    ctr = vis.get_view_control()
    ctr.rotate(50, 0)  # no idea the units here

    # capture the image (colored)
    image = np.asarray(vis.capture_screen_float_buffer())

    # capture the depth (slow)
    if DEPTH:
        depth = np.asarray(vis.capture_depth_float_buffer())
        depth = np.repeat(np.expand_dims(depth, 2), 3, 2) / depth.max()
        image = np.column_stack((image, depth))

    plt.imshow(image)
    plt.axis('off')
    plt.savefig(f"{o_temp}/{str(count).zfill(2)}.png")

    count += 1
    if count > 40:
        x = 0/0  # idk how to stop it, this works

    return False


def generate_gif(f):
    """
    generate gif from a bunch of images
    """
    pattern = f.split("/")[-1].split(".")[0]
    file_list = glob.glob(f'{o_temp}/*.png')
    file_list.sort()
    images = [imageio.imread(f) for f in file_list]
    imageio.mimsave(f'{f_root}/{pattern}.gif', images)


pcd = o3d.io.read_point_cloud(f)

try:
    o3d.visualization.draw_geometries_with_animation_callback(
        [pcd], rotate_view, width=800, height=1200)
except ZeroDivisionError:
    pass  # Done!

generate_gif(f)
