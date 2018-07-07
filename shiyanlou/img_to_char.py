from PIL import Image
import argparse

ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")


parser = argparse.ArgumentParser()

parser.add_argument('file')
parser.add_argument('-o', '--output')
parser.add_argument('--width')