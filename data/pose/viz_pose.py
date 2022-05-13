
import json
from matplotlib import pyplot as plt

F = "BJ721E05W-J11@9=person_whole_front_keypoints"
with open(f"data/pose/{F}.json") as f:
    data = json.loads(f.read())

print(data)

HEIGHT, WIDTH = 512, 320

for person in data["people"]:

    for point_type in ("pose_keypoints_2d", "face_keypoints_2d", "hand_left_keypoints_2d", "hand_right_keypoints_2d"):
        xs, ys = [], []
        keypoints = person[point_type]
        for i in range(len(keypoints) // 3):
            x, y, p = keypoints[3*i], keypoints[3*i+1], keypoints[i*3+2]
            xs.append(x)
            ys.append(HEIGHT - y)
            # print(x, y)
        plt.scatter(xs, ys, label=point_type)

plt.legend()
plt.xlim((0, WIDTH))
plt.ylim((0, HEIGHT))
fig = plt.gcf()
fig.set_size_inches(WIDTH/50, HEIGHT/50)
plt.savefig(f"data/pose/demo-{F}.png")
