# Content-Maker
Automated Short-Form Content 

This script takes a source video, randomly extracts a few frames, then creates a short montage video from those frames with fade-in/fade-out transitions and background music. After rendering, it deletes the temporary frames folder.

## What it does
1. Loads the video - https://www.youtube.com/watch?v=miXp7gpguJU - if you want this work you have to download this video and load it yourself, its 1 hour long and too big to put in this repo.
2. Randomly selects **5 timestamps** across the video duration
3. Saves extracted frames as `frame_0.jpg ... frame_4.jpg`
4. Builds a montage where each frame is shown for ~4.2 seconds with fades
5. Adds an audio track (`.mp3`) with fade-in and fade-out
6. Exports the final video (`.mp4`)
7. Deletes the extracted frames folder to clean up


- Python 3.9+

### Packages
- `moviepy`
- `pytube` (imported, not required unless you add YouTube downloading)
- `imageio`
- `ffmpeg`

### Install
```bash
pip install -U moviepy pytube imageio
