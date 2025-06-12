import os
import shutil

import dotenv
import numpy as np
import pandas as pd
import huggingface_hub
import matplotlib.pyplot as plt
import tifffile
import matplotlib.patches as mpatches

from forest import paths

def download_data():
    # The repository of this data is private
    #    - Make a new account
    #    - Ask to be added to the repo by the supervisor
    #    - Go to https://huggingface.co/settings/tokens
    #    - Generate a token
    #    - In your terminal write:
    #      ```
    #      export HUGGINGFACE_TOKEN=your_token_here
    #      ```
    #    - Then run the script as normal
    #      ```
    #      python loading_data.py
    #      ```

    # Download target folder relative to current path
    out_folder = "raw/forest-plot-analysis"

    # Example data repository name
    repository = "remote-sensing-ense3-grenoble-inp/forest-plot-analysis"

    dotenv.load_dotenv()
    token = os.getenv("HUGGINGFACE_TOKEN")

    data_path = paths.data()
    target_directory = data_path / out_folder
    if not target_directory.exists():
        if token is None:
            raise ValueError(
                "The repository forest requires a token.\n" +
                "From the project root folder, copy .env.developement to " +
                ".env and ask your supervisor to type the token there.\n" +
                "Please save this file in a safe place for future downloads."
            )
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
                "Error downloading repository.\n" +
                f"{e}"
            )


def visualize_data():
    filename_hsi = {
        "1": "raw/forest-plot-analysis/data/hi/1.tif",
        "1b": "raw/forest-plot-analysis/data/hi/1b.tif",
        "2": "raw/forest-plot-analysis/data/hi/2.tif",
        "3": "raw/forest-plot-analysis/data/hi/3.tif",
        "3b": "raw/forest-plot-analysis/data/hi/3b.tif",
        "4": "raw/forest-plot-analysis/data/hi/4.tif",
        "Premol": "raw/forest-plot-analysis/data/hi/Premol.tif",
    }

    filename_label = "raw/forest-plot-analysis/data/gt/df_pixel.csv"
    plot_id = "1"
    rgb_channels = [64, 28, 15]
    filename_hsi = filename_hsi[plot_id]

    data_path = paths.data()
    file_hsi = data_path / filename_hsi
    file_label = data_path / filename_label

    rgb_array = tifffile.TiffFile(file_hsi)
    rgb_array = rgb_array.asarray()
    rgb_array = rgb_array[:, :, rgb_channels]
    for i in range(rgb_array.shape[2]):
        min_val = np.percentile(rgb_array[..., i], 2)
        max_val = np.percentile(rgb_array[..., i], 98)
        rgb_array[..., i] = np.clip((rgb_array[..., i] - min_val) / (max_val - min_val), 0, 1)


    rgb_array = rgb_array / rgb_array.max()

    df = pd.read_csv(file_label)
    df = df[df["plotid"] == plot_id]
    img_label = np.zeros((rgb_array.shape[0], rgb_array.shape[1], 3))

    tree_ids = df["specie"].unique()
    color_map = {
        tree_id: color for tree_id, color
        in zip(tree_ids, plt.cm.tab20.colors)
    }
    for _, row in df.iterrows():
        color = color_map[row["specie"]]
        img_label[int(row["row"]), int(row["col"])] = color

    fig, ax = plt.subplots(1, 1)
    ax.imshow(rgb_array)
    ax.set_title("Hyperspectral image")
    ax.imshow(img_label, alpha=0.5)
    ax.set_title("Labels map")
    legend_elements = [
        mpatches.Patch(color=color, label=class_name)
        for class_name, color in color_map.items()
    ]
    ax.legend(
        handles=legend_elements,
        loc='upper right',
        bbox_to_anchor=(1.25, 1),
        title="Classes",
    )

    output_path = data_path / "outputs/demo.png"
    fig.savefig(output_path)
    print(f"Image saved to {output_path}")
    plt.close(fig)


def main():
    download_data()
    visualize_data()

if __name__ == "__main__":
    main()