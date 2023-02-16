import sys
from run import run
from video import create_video
from dotenv import load_dotenv
import os
def main(session):

    load_dotenv('.env')
    #run(session)
    if os.getenv('DEBUG') == "1":
        create_video(session)

if __name__ == "__main__":
    for session in sys.argv[1:]:
        main(session) 