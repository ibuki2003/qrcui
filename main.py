import decoder
import encoder
import magic
import sys
import argparse
import cv2
import numpy as np

READ_BLOCK_SIZE = 1024

def main():
    parser = argparse.ArgumentParser(description='QR reader on CUI')

    parser.add_argument('-i', '--input', help='specify input file instead of arg (- or empty to use stdin)')
    parser.add_argument('-p', '--ascii', help='output QR with ASCII chars instead of image', action='store_true')
    parser.add_argument('-d', '--debug', help='show details about decoded codes', action='store_true')
    parser.add_argument('str', nargs='*', help='string for making qr')


    args = parser.parse_args()
    mode, ret = process(args)
    if mode == False:
        if args.debug:
            for code in ret:
                print(code.type, '\t', code.data)
        else:
            if len(ret)==0:
                sys.exit(-1)

            sys.stdout.buffer.write(ret[0].data)
    else:
        if args.ascii:
            encoder.show_ascii_qr(ret)
        else:
            img = encoder.make_qr(ret)
            if sys.stdout.isatty():
                img.show()
            else:
                img.save(sys.stdout.buffer)

def process(args):
    if args.input is not None:
        if args.input == '-': # stdin
            return read_stdin()
        else:
            return read_file(args.input)
    else:
        if args.str is None or len(args.str)==0:
            if sys.stdin.isatty():
                return False, decoder.capture_qr()
            else:
                return read_stdin()
        else:
            return True, ' '.join(args.str)

def read_stdin():
    input_buf = sys.stdin.buffer.read()
    if magic.from_buffer(input_buf, mime=True).startswith('image/'):
        nparr = np.frombuffer(input_buf, np.uint8)
        img_np = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        return False, decoder.read_qr(img_np)
    else:
        return True, input_buf

def read_file(path):
    if magic.from_file(path, mime=True).startswith('image/'):
        return False, decoder.read_qr(cv2.imread(path))
    else:
        with open(path, 'rb') as f:
            input_buf = f.read()
        return True, input_buf


if __name__ == '__main__':
    main()
