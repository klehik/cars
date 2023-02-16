import os
from metadata import get_metadata
import pandas as pd
from find_location import find_car_location
import time
from video import create_video

def run(session):
    print(f'Processing session {session}')
    st = time.time()

    # session dir
    session_path = f'./original/{session}'
    dir_list = os.listdir(session_path)
    # find .txt file
    for dir in dir_list:
        if '.txt' in dir:
            text_file = dir
            break
    
    with open(f'{session_path}/{text_file}') as f:
        line = f.readline()
        area_x = float(line)
    
    dir_list.remove(dir)
    dir_list.remove('000')
    if '.DS_Store' in dir_list:
        dir_list.remove('.DS_Store')
    dir_list.sort()

    # target dir
    target_dir = f'./edited/{session}'
    if not os.path.exists(target_dir):
        os.mkdir(target_dir)
        
    base_filename = f'{session}-000-003-.jpg'
    #measure_filename = '000-0000.jpg'
    
    data_all = []
    for dir in dir_list:
        
        car_dir = f'{target_dir}/{dir}'
        if not os.path.exists(car_dir):
            os.mkdir(car_dir)

        filelist = os.listdir(f'{session_path}/{dir}')
        filelist.sort()
        for filename in filelist:
            base_image_path = f'{session_path}/{dir}/{base_filename}'
            if filename != base_image_path:
                #print(session, dir, filename)
                
                imagepath = f'{session_path}/{dir}/{filename}'
                data = get_metadata(imagepath)
                data['filename'] = filename
                data['session'] = session
                data['car_id'] = dir
                location = find_car_location(imagepath, filename, dir, session) 

                data['area_width_cm'] = area_x
                data['location_x'] = location[0]
                data['location_y'] = location[1]
                data['distance_cm'] = round(area_x / data['image_size'][0] * location[0], 2)
                
                
                data_all.append(data)
        


    df = pd.DataFrame(data_all)
    df = df.sort_values(['car_id', 'filename'])
    df.reset_index(inplace=True, drop=True)
    df.to_csv(f'./data/{session}.csv')

    et = time.time()

    # get the execution time
    elapsed_time = et - st
    print('Execution time:', elapsed_time, 'seconds')
    