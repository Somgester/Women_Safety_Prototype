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


#video 11