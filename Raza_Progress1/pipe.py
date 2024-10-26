import cv2
import mediapipe as mp
import time
import numpy as np

# Initialize MediaPipe Holistic model
mp_holistic = mp.solutions.holistic
holistic = mp_holistic.Holistic(static_image_mode=False)

# Capture webcam input
cap = cv2.VideoCapture(0)
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

fps = 10
duration = 5  # seconds
frame_count = fps * duration

frames = []
landmarks_data = []

# Start recording for 5 seconds
print("Recording started...")
start_time = time.time()
while len(frames) < frame_count:
    ret, frame = cap.read()
    if not ret:
        print("Failed to capture frame.")
        break

    frames.append(frame)

    # Convert BGR image to RGB for processing
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    # Process with holistic model
    results = holistic.process(rgb_frame)
    
    # Save pose, face, and hand landmarks
    pose_landmarks = results.pose_landmarks
    face_landmarks = results.face_landmarks
    left_hand_landmarks = results.left_hand_landmarks
    right_hand_landmarks = results.right_hand_landmarks

    # Prepare vectors
    frame_landmarks = {}

    if pose_landmarks:
        frame_landmarks['pose'] = np.array([[lm.x, lm.y, lm.z] for lm in pose_landmarks.landmark])
    
    if face_landmarks:
        frame_landmarks['face'] = np.array([[lm.x, lm.y, lm.z] for lm in face_landmarks.landmark])

    if left_hand_landmarks:
        frame_landmarks['left_hand'] = np.array([[lm.x, lm.y, lm.z] for lm in left_hand_landmarks.landmark])
    
    if right_hand_landmarks:
        frame_landmarks['right_hand'] = np.array([[lm.x, lm.y, lm.z] for lm in right_hand_landmarks.landmark])
    
    landmarks_data.append(frame_landmarks)

    if time.time() - start_time >= duration:
        break

cap.release()
print("Recording finished.")

# Function to return the data points as vectors
def get_landmarks_as_vectors(landmarks_data):
    vectors = []
    for frame in landmarks_data:
        frame_vectors = {}
        if 'pose' in frame:
            frame_vectors['pose'] = frame['pose']
        if 'face' in frame:
            frame_vectors['face'] = frame['face']
        if 'left_hand' in frame:
            frame_vectors['left_hand'] = frame['left_hand']
        if 'right_hand' in frame:
            frame_vectors['right_hand'] = frame['right_hand']
        
        vectors.append(frame_vectors)
    return vectors

# Get the landmarks as vectors
landmarks_vectors = get_landmarks_as_vectors(landmarks_data)

# Output the vectors for each frame
for i, vectors in enumerate(landmarks_vectors):
    print(f"Frame {i+1}:")
    for landmark_type, coords in vectors.items():
        print(f"  {landmark_type}: {coords}")