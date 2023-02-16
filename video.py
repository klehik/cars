from moviepy.editor import *

def create_video(session):

    path = f'./edited/{session}'

    dir_list = os.listdir(path)
    dir_list.sort()
    image_clips = []

    ignored = ['.DS_Store']

    print('creating video..')
    for dir in dir_list:
        if dir not in ignored:
            filelist = os.listdir(f'{path}/{dir}')
            filelist.sort()
            for file in filelist:
                
                if file not in ignored:
                    ic = ImageClip(f'{path}/{dir}/{file}').set_duration(0.1).resize((750,328))
                    image_clips.append(ic)


    video = concatenate_videoclips(image_clips, method="chain")
    video.write_videofile(f'videos/{session}.mp4', codec='mpeg4', fps=12)


