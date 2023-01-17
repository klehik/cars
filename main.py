import sys
from directory import run
def main(session):

    run(session)

    



if __name__ == "__main__":
    session = str(sys.argv[1])
    main(session) 