import shutil

import huggingface_hub
import cv2
import matplotlib.pyplot as plt
import matplotlib.patches as patches

from rs_video import paths

def download_data():
    # Download target folder relative to current path
    out_folder = "raw/rs-video-beach"

    # Example data repository name
    repository = "remote-sensing-ense3-grenoble-inp/rs-video-beach"

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
    # Load video
    video_path = "raw/rs-video-beach/data/beach.mp4"

    data_path = paths.data()

    cap = cv2.VideoCapture(data_path / video_path)

    # Frame number to capture (e.g., 100th frame)
    frame_number = 6
    cap.set(cv2.CAP_PROP_POS_FRAMES, frame_number)

    # Read the frame
    ret, frame = cap.read()
    if ret is None:
        print("Failed to capture the frame.")
    cap.release()
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    fig, ax = plt.subplots()
    ax.imshow(frame_rgb)
    fig.savefig(data_path / "outputs/demo.png")
    plt.close(fig)


def main():
    download_data()
    visualize_data()


if __name__ == "__main__":
    main()