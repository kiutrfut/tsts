import requests
from tqdm import tqdm

url = "https://example.com/file.mp4"
filename = "file.mp4"

response = requests.get(url, stream=True)
total_size = int(response.headers.get("content-length", 0))
block_size = 1024  # 1 Kibibyte

with open(filename, "wb") as f:
    with tqdm(total=total_size, unit="iB", unit_scale=True) as progress_bar:
        for data in response.iter_content(block_size):
            f.write(data)
            progress_bar.update(len(data))

print("Download complete!")
