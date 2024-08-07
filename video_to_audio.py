import os
import subprocess
from datetime import datetime

def video_to_audio(video_path):
    # Get the directory and filename (without extension) of the input file
    video_dir = os.path.dirname(video_path)
    video_filename = os.path.splitext(os.path.basename(video_path))[0]
    
    # Generate output filename (using video filename and current timestamp)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_filename = f"{video_filename}_audio_{timestamp}.mp3"
    
    # Create full path for output file in the same directory as the video
    output_path = os.path.join(video_dir, output_filename)
    
    # Construct FFmpeg command
    command = [
        "ffmpeg",
        "-i", video_path,  # Input file
        "-q:a", "0",       # Highest quality audio extraction
        "-map", "a",       # Select only the audio stream
        "-y",              # Overwrite existing file
        output_path        # Output file
    ]
    
    try:
        # Execute FFmpeg
        subprocess.run(command, check=True, stderr=subprocess.PIPE)
        print(f"Audio extraction completed. Output file: {output_path}")
        return output_path
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e.stderr.decode()}")
        return None

if __name__ == "__main__":
    video_path = input("Enter the path to the video file: ")
    video_to_audio(video_path)
