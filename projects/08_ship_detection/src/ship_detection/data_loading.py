import shutil
import json

import imageio
import huggingface_hub
import matplotlib.pyplot as plt
import matplotlib.patches as patches

from ship_detection import paths

def download_data():
    # Download target folder relative to current path
    out_folder = "raw/ship-detection"

    # Example data repository name
    repository = "remote-sensing-ense3-grenoble-inp/ship-detection"

    data_path = paths.data()
    target_directory = data_path / out_folder
    if not target_directory.exists():
        try:
            target_directory.mkdir(parents=True, exist_ok=True)
            huggingface_hub.snapshot_download(
                repo_id=repository,
                repo_type="dataset",
                local_dir=target_directory,
            )
        except Exception as e:
            shutil.rmtree(target_directory)
            raise ValueError(
                "Error downloading repository." +
                f"{e}"
            )

def visualize_data():
    filename_rgb = "raw/ship-detection/data/1.png"
    filename_bb = "raw/ship-detection/data/metadata.jsonl"

    data_path = paths.data()
    file_rgb = data_path / filename_rgb
    file_bb = data_path / filename_bb

    img = imageio.v3.imread(file_rgb)

    with open(file_bb) as file_bb_opened:
        jsonl_content = [json.loads(line) for line in file_bb_opened]
    ann = next((a for a in jsonl_content if a["file_name"] == file_rgb.name))

    fig, ax = plt.subplots()
    ax.imshow(img)
    for bbox in ann['objects']['bbox']:
        # bounding box format: [xmin, ymin, xmax, ymax]
        rect = patches.Rectangle(
            (bbox[0], bbox[1]),
            bbox[2] - bbox[0],
            bbox[3] - bbox[1],
            linewidth=2,
            edgecolor='red',
            facecolor='none',
            linestyle='-'
        )
        ax.add_patch(rect)

    fig.savefig(data_path / "outputs/demo.png")
    plt.close(fig)


def main():
    download_data()
    visualize_data()


if __name__ == "__main__":
    main()