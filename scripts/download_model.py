"""Download the verified demo model from Google; never commit model binaries."""
from pathlib import Path
import hashlib
import urllib.request

ROOT = Path(__file__).resolve().parent.parent
URL = 'https://storage.googleapis.com/mediapipe-models/pose_landmarker/pose_landmarker_lite/float16/latest/pose_landmarker_lite.task'
SHA256 = '59929e1d1ee95287735ddd833b19cf4ac46d29bc7afddbbf6753c459690d574a'

def main():
    destination = ROOT / 'models' / 'pose_landmarker_lite.task'
    destination.parent.mkdir(exist_ok=True)
    if destination.exists() and hashlib.sha256(destination.read_bytes()).hexdigest() == SHA256:
        print('Verified pose model is already available.')
        return
    print('Downloading MediaPipe Pose Landmarker Lite from Google...')
    with urllib.request.urlopen(URL, timeout=60) as response:
        data = response.read(20 * 1024 * 1024)
    if hashlib.sha256(data).hexdigest() != SHA256:
        raise RuntimeError('Model hash changed. Check the official model release before updating; existing file preserved.')
    temporary = destination.with_suffix('.part')
    temporary.write_bytes(data)
    temporary.replace(destination)
    print('Model downloaded and SHA-256 verified.')

if __name__ == '__main__':
    main()
