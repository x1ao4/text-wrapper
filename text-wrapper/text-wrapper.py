input_file = 'input.txt'
output_file = 'output.txt'

prefix = 'prefix '
suffix = ' suffix'

with open(input_file, 'r', encoding='utf-8') as f_in, open(output_file, 'w', encoding='utf-8') as f_out:
    for line in f_in:
        f_out.write(prefix + line.strip() + suffix + '\n')
