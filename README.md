# Video to Audio Converter

This Python script extracts audio from a video file using FFmpeg.

## Features

- Extracts audio from video files
- Saves the audio in the same directory as the video
- Generates unique filenames using timestamps
- Uses FFmpeg for high-quality audio extraction

## Requirements

- Python 3.x
- FFmpeg (must be installed and accessible in the system PATH)

## Installation

1. Ensure you have Python 3.x installed on your system.
2. Install FFmpeg if you haven't already. You can download it from [ffmpeg.org](https://ffmpeg.org/).
3. Make sure FFmpeg is added to your system's PATH.
4. Download the `video_to_audio.py` script to your local machine.

## Usage

1. Open a terminal or command prompt.
2. Navigate to the directory containing the `video_to_audio.py` script.
3. Run the script using Python:

   ```
   python video_to_audio.py
   ```

4. When prompted, enter the full path to your video file.
5. The script will process the video and save the extracted audio in the same directory as the video file.

## Output

The extracted audio file will be saved in MP3 format with a filename in the following format:

```
[original_video_name]_audio_[YYYYMMDD_HHMMSS].mp3
```

For example, if your input video is named "my_video.mp4", the output might be "my_video_audio_20240807_123456.mp3".

## Error Handling

If an error occurs during the extraction process, the script will display an error message with details about the problem.

## Notes

- This script uses FFmpeg's highest quality settings for audio extraction. You can modify the FFmpeg command in the script if you need different output settings.
- Make sure you have the necessary permissions to read the input video file and write to the output directory.

## License

This project is open source and available under the [MIT License](https://opensource.org/licenses/MIT).

## Contributing

Contributions, issues, and feature requests are welcome. Feel free to check issues page if you want to contribute.

## Support

If you encounter any problems or have any questions, please open an issue in the GitHub repository.
