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
FOLDER = "/Users/anna/Git/aspfohl/deeep-learning/results"
SAMPLE = "person"
DEPTH = True
# -------------------------------------------------------


f = f"{FOLDER}/aligned/pcd/test_pairs/{SAMPLE}.ply"
o = f"{FOLDER}/gifs/{SAMPLE}"

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
    image = vis.capture_screen_float_buffer()
    plt.imshow(np.asarray(image))
    plt.savefig(f"{o}/image{str(count).zfill(2)}.png")

    # capture the depth (slow)
    if DEPTH:
        depth = vis.capture_depth_float_buffer()
        plt.imshow(np.asarray(depth))
        plt.savefig(f"{o}/depth{str(count).zfill(2)}.png")

    count += 1
    if count > 40:
        x = 0/0  # idk how to stop it, this works

    return False


def generate_gif(pattern):
    """
    generate gif from a bunch of images
    """
    file_list = glob.glob(f'{o}/{pattern}*.png')
    file_list.sort()
    images = [imageio.imread(f) for f in file_list]
    imageio.mimsave(f'{o}/{pattern}.gif', images)


pcd = o3d.io.read_point_cloud(f)

try:
    o3d.visualization.draw_geometries_with_animation_callback(
        [pcd], rotate_view, width=800, height=1200)
except ZeroDivisionError:
    pass  # Done!

generate_gif("image")
if DEPTH:
    generate_gif("depth")
