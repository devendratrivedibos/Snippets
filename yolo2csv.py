import os
import pandas as pd
image_width , image_height = 2464,2056




class_map ={
  0: "Speed_Limit",
  1: "Petrol_Pump",
  2: "SIGNBOARD_HAZARD",
  3: "Narrow_Bridge",
  4: "U_turn_prohibited",
  5: "Road_Merge",
  6: "Pedestrian_Crossing",
  7: "Speed_Breaker",
  8: "U_turn_ahead",
  9: "Service_road_start",
  10: "Left_Turn",
  11: "Go Slow",
  12: "Right_turn",
  13: "P_Road_split",
  14: "busstop",
  15: "signboard",
  16: "X",
  17: "School_ahead",
  18: "T-Sign",
  19: "STOP",
  20: "Highway_code",
  21: "No Parking",
  22: "SlipperyRoad",
  23: "Landslide_Danger",
  24: "Give Way",
  25: "Road_Diverge",
  26: "Compulsary_turn_left",
  27: "Collision_area",
  28: "DANGER",
  30: "No Right Turn"

}



# Define the function to convert YOLO format to x1, y1, x2, y2
def yolo_to_xywh(image_width, image_height, center_x, center_y, width, height):
    x1 = int((center_x - width / 2) * image_width)
    y1 = int((center_y - height / 2) * image_height)
    x2 = int((center_x + width / 2) * image_width)
    y2 = int((center_y + height / 2) * image_height)
    return x1, y1, x2, y2

# Define the folder path containing the YOLO annotations
folder_path =  r'E:\Traffic_Sign_data\7c522331-cea5-4438-9f34-f87882bfbec3\data_set'

# Get a list of all the .txt files in the folder
file_list = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith('.txt')]

# Create an empty list to store the output
output_list = []

# Loop through each file and convert the annotations
for file_path in file_list:
    # Get the image name from the file path
    image_name = os.path.splitext(os.path.basename(file_path))[0]
    # Read the file
    with open(file_path, 'r') as f:
        data = f.read().splitlines()
    # Loop through each line of the file and convert the annotations
    for line in data:
        class_id, center_x, center_y, width, height = map(float, line.split())
        x1, y1, x2, y2 = yolo_to_xywh(image_width, image_height, center_x, center_y, width, height)
        output_list.append([image_name, class_id, x1, y1, x2, y2])

# Convert the list of outputs to a pandas DataFrame
df = pd.DataFrame(output_list, columns=['image_name', 'class_id', 'x1', 'y1', 'x2', 'y2'])
# Map the class IDs to strings
df['class'] = df['class_id'].map(class_map)
# Save the DataFrame to a .csv file
df.to_csv(r'E:\Traffic_Sign_data\7c522331-cea5-4438-9f34-f87882bfbec3\data_set\output.csv', index=False)