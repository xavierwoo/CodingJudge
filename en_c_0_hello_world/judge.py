import os
import sys
sys.path.append("../.common")
from common import main

if __name__ == "__main__":
    main(os.path.dirname(os.path.realpath(__file__)), sys.argv)
