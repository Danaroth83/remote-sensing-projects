import os
import shutil

import numpy as np
import huggingface_hub
import matplotlib.pyplot as plt
from scipy.io import loadmat
import tifffile

from snow_ts import paths


def download_data():
    # Download target folder relative to current path
    out_folder = "raw/modis-snow-coverage"

    # Example data repository name
    repository = "remote-sensing-ense3-grenoble-inp/modis-snow-coverage"

    data_path = paths.data()
    target_directory = data_path / out_folder
    if not target_directory.exists():
        try:
            target_directory.mkdir(parents=True, exist_ok=True)
            huggingface_hub.snapshot_download(
                repo_id=repository,
                repo_type="dataset",
                local_dir=target_directory,
                token=os.getenv("HUGGINGFACE_TOKEN"),
            )
        except Exception as e:
            shutil.rmtree(target_directory)
            raise ValueError(
                "Error downloading repository." +
                f"{e}"
            )


def visualize_data():
    filename_hsi = "raw/modis-snow-coverage/data/2013039/Modimlab_2013039_reproj2.tif"
    filename_mat = "raw/modis-snow-coverage/data/2013039/Spot_degrade_2013039.mat"
    data_path = paths.data()
    file_hsi = data_path / filename_hsi
    file_mat = data_path / filename_mat

    mat_handler = loadmat(file_mat)
    array_spot = mat_handler["Spot_degrade"]

    rgb_channels = [0, 3, 2]

    array = tifffile.imread(file_hsi)
    array = np.nan_to_num(array, nan=0.0)
    rgb_array = array[:, :, rgb_channels]
    rgb_array = rgb_array / rgb_array.max()

    fig, ax = plt.subplots(1, 2)
    ax[0].imshow(rgb_array)
    ax[0].set_title("MODIS acquisition")
    ax[1].imshow(array_spot, cmap="gray")
    ax[1].set_title("SPOT reference")

    output_path = data_path / "outputs/demo.png"
    fig.savefig(output_path)
    print(f"Image saved to {output_path}")
    plt.close(fig)


def main():
    download_data()
    visualize_data()

if __name__ == "__main__":
    main()