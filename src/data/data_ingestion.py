import os
import gdown

# Original Google Drive view URLs
train_url = "https://drive.google.com/file/d/1E7-7EoGmGDRNrFIdESeDjc52EwyshpWQ/view?usp=sharing"
val_url = "https://drive.google.com/file/d/11lefSA6uS8Xu6TqDbn3uRchEd_j0197r/view?usp=sharing"

# Extract file IDs
train_file_id = "1E7-7EoGmGDRNrFIdESeDjc52EwyshpWQ"
val_file_id = "11lefSA6uS8Xu6TqDbn3uRchEd_j0197r"

# Create output directory
output_dir = "data/raw"
os.makedirs(output_dir, exist_ok=True)

# Full output file paths
train_output_path = os.path.join(output_dir, "train.zip")
val_output_path = os.path.join(output_dir, "val.zip")

# Convert file IDs to downloadable URLs
train_download_url = f"https://drive.google.com/uc?id={train_file_id}"
val_download_url = f"https://drive.google.com/uc?id={val_file_id}"

# Download the ZIP files
gdown.download(url=train_download_url, output=train_output_path, quiet=False)
gdown.download(url=val_download_url, output=val_output_path, quiet=False)