# import cv2
# import os

# def extract_frames(video_path, output_folder='frames', frame_interval=30):
#     # Create output directory if it doesn't exist
#     if not os.path.exists(output_folder):
#         os.makedirs(output_folder)
    
#     # Open the video file
#     cap = cv2.VideoCapture(video_path)
#     frame_count = 0
#     extracted_frame_count = 0
    
#     while True:
#         ret, frame = cap.read()
#         if not ret:
#             break
        
#         # Save frame at specified intervals
#         if frame_count % frame_interval == 0:
#             frame_filename = os.path.join(output_folder, f"frame_{extracted_frame_count:04d}.jpg")
#             cv2.imwrite(frame_filename, frame)
#             print(f"Saved frame {extracted_frame_count} to {frame_filename}")
#             extracted_frame_count += 1
        
#         frame_count += 1

#     cap.release()
#     print("Finished extracting frames")

# # Example usage
# extract_frames('videos/video3.mp4')


#for images

import cv2
import os

def extract_frames(video_path, output_folder='Dataset11', frame_interval=15, start_time=0, end_time=None):
    # Create output directory if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Open the video file
    cap = cv2.VideoCapture(video_path)
    
    # Get video properties
    fps = cap.get(cv2.CAP_PROP_FPS)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    duration = total_frames / fps
    
    if end_time is None:
        end_time = duration
    
    # Convert start and end time to frame indices
    start_frame = int(start_time * fps)
    end_frame = min(int(end_time * fps), total_frames)
    
    if start_frame >= total_frames or end_frame <= start_frame:
        print("Invalid time range")
        return

    frame_count = 0
    extracted_frame_count = 0
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        if start_frame <= frame_count < end_frame:
            # Save frame at specified intervals
            if frame_count % frame_interval == 0:
                frame_filename = os.path.join(output_folder, f"frame_{extracted_frame_count:04d}.jpg")
                cv2.imwrite(frame_filename, frame)
                print(f"Saved frame {extracted_frame_count} to {frame_filename}")
                extracted_frame_count += 1
        
        if frame_count >= end_frame:
            break
        
        frame_count += 1

    cap.release()
    print("Finished extracting frames")

# Example usage
extract_frames('videos/video8.mp4', start_time=5, end_time=28)





#for videos

import cv2
import os

def extract_video_segment(video_path, output_folder='NonHarassmentVideo', start_time=500, end_time=510):

    # Create the output directory if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Define the output video path
    output_path = os.path.join(output_folder, 'segment40.mp4')
    
    # Check if the video file exists
    if not os.path.isfile(video_path):
        print(f"Error: The file {video_path} does not exist.")
        return
    
    # Open the video file
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Error: Unable to open video file.")
        return
    
    # Get video properties
    fps = cap.get(cv2.CAP_PROP_FPS)
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Define the codec for the output video
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    
    # Calculate start and end frame
    start_frame = int(start_time * fps)
    end_frame = int(end_time * fps)
    
    # Set up the video writer
    out = cv2.VideoWriter(output_path, fourcc, fps, (frame_width, frame_height))
    
    # Initialize frame count
    frame_count = 0
    
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Unable to read frame or end of video reached.")
            break
        
        if frame_count > end_frame:
            break
        
        if start_frame <= frame_count <= end_frame:
            out.write(frame)
        
        frame_count += 1
    
    cap.release()
    out.release()
    print(f"Video segment saved to {output_path}")

# Example usage
extract_video_segment('NonHarassmentVideo/extracted_segment.mp4', start_time=500, end_time=510)
