import shutil

import numpy as np
import huggingface_hub
import tifffile
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap, BoundaryNorm
import matplotlib.patches as mpatches

from urban import paths


def download_data():
    # Download target folder relative to current path
    out_folder = "raw/openearthmap-paris"

    # Example data repository name
    repository = "remote-sensing-ense3-grenoble-inp/openearthmap-paris"

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
    filename_rgb = "raw/openearthmap-paris/data/paris/images/paris_1.tif"
    filename_label = "raw/openearthmap-paris/data/paris/labels/paris_1.tif"

    data_path = paths.data()
    file_rgb = data_path / filename_rgb
    file_label = data_path / filename_label

    rgb_array = tifffile.TiffFile(file_rgb)
    rgb_array = rgb_array.asarray()
    rgb_array = rgb_array / rgb_array.max()

    label_array = tifffile.TiffFile(file_label)
    label_array = label_array.asarray()

    class_colors = {
        "Bareland": "#800000",
        "Rangeland": "#00FF24",
        "Developed space": "#949494",
        "Road": "#FFFFFF",
        "Tree": "#226126",
        "Water": "#0045FF",
        "Agriculture land": "#4BB549",
        "Building": "#DE1F07",
    }

    cmap = ListedColormap(list(class_colors.values()))
    norm = BoundaryNorm(boundaries=np.arange(1, len(class_colors) + 1), ncolors=len(class_colors))

    fig, ax = plt.subplots(1, 2, figsize=(12, 6))
    ax[0].imshow(rgb_array)
    ax[0].set_title("RGB image")
    ax[1].imshow(label_array, cmap=cmap, norm=norm)
    ax[1].set_title("Labels map")

    legend_elements = [
        mpatches.Patch(color=color, label=class_name)
        for class_name, color in class_colors.items()
    ]
    ax[1].legend(
        handles=legend_elements,
        loc='upper right',
        bbox_to_anchor=(1.25, 1),
        title="Classes",
    )
    
    fig.savefig(data_path / "outputs/demo.png")
    plt.close(fig)


def main():
    download_data()
    visualize_data()


if __name__ == "__main__":
    main()