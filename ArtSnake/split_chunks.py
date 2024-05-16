import os

def split_binary_file(input_file, output_prefix, num_parts):
    total_size = os.path.getsize(input_file)
    part_size = total_size // num_parts
    
    with open(input_file, 'rb') as infile:
        file_data = infile.read()
    
    part_sizes = [min(part_size, len(file_data)) for _ in range(num_parts)]
    remaining_size = total_size - sum(part_sizes)
    part_sizes[-1] += remaining_size 
    
    for i, part_size in enumerate(part_sizes, start=1):
        with open(f'{output_prefix}part{i}.bin', 'wb') as outfile:
            outfile.write(file_data[:part_size])
            file_data = file_data[part_size:]  

input_file = 'data\\27kpng_model_best.pth.tar' #give the path of the file you want to split
output_prefix = 'split_'
num_parts = 4 
split_binary_file(input_file, output_prefix, num_parts)
