def merge_parts(num_parts, prefix='split_', output_file='merged_file.tar'):
    with open(prefix + 'part1.bin', 'rb') as f1, open(output_file, 'wb') as outfile:
        outfile.write(f1.read())
        
    for i in range(2, num_parts + 1):
        with open(prefix + f'part{i}.bin', 'rb') as f:
            with open(output_file, 'ab') as outfile:
                outfile.write(f.read())

def main ():
    num_parts = 4
    merge_parts(num_parts)


if __name__ == '__main__':
    main()