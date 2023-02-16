import sys
from run import run
from video import create_video
from dotenv import load_dotenv
import os

def main(session):
    load_dotenv('.env')
    if os.getenv('PROCESS') == "1":
        run(session)
    if os.getenv('DEBUG_VIDEO') == "1":
        create_video(session)

if __name__ == "__main__":
    for session in sys.argv[1:]:
        main(session) 