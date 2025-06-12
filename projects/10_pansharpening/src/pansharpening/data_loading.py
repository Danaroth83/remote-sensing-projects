import os
import shutil

import dotenv
import numpy as np
import huggingface_hub
import matplotlib.pyplot as plt
import imageio

from pansharpening import paths

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
    out_folder = "raw/spot-pansharpening"

    # Example data repository name
    repository = "remote-sensing-ense3-grenoble-inp/spot-pansharpening"

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
                token=token,
            )
        except Exception as e:
            shutil.rmtree(target_directory)
            raise ValueError(
                "Error downloading repository." +
                f"{e}"
            )


def visualize_data():
    filename_ms = "raw/spot-pansharpening/data/1.TIF"
    filename_pan = "raw/spot-pansharpening/data/3.TIF"

    data_path = paths.data()
    file_ms = data_path / filename_ms
    file_pan = data_path / filename_pan

    img_ms = imageio.v3.imread(file_ms)
    img_ms = np.moveaxis(img_ms,[-3, -2, -1], [2, 0, 1])
    img_ms = img_ms / 255
    img_pan = imageio.v3.imread(file_pan)
    img_pan = np.moveaxis(img_pan, [-2, -1], [0, 1])
    img_pan = img_pan / 255

    fig, ax = plt.subplots(1, 2)
    ax[0].imshow(img_ms)
    ax[0].set_title("Multispectral")
    ax[1].imshow(img_pan, cmap="gray")
    ax[1].set_title("Panchromatic")

    output_path = data_path / "outputs/demo.png"
    fig.savefig(output_path)
    print(f"Image saved to {output_path}")
    plt.close(fig)


def main():
    download_data()
    visualize_data()


if __name__ == "__main__":
    main()