from pathlib import Path
import json
import os
directory_of_current_file = os.path.dirname(__file__)
os.chdir(directory_of_current_file)

input_file = 'numbers.json'
file_content = Path(input_file).read_text(encoding='utf-8')
numbers = json.loads(file_content)

product = 1
for num in numbers:

    if num % 3 == 0:
        print(f'Tittei! {num} kan deles på 3')
    else:
        print(f'Tittei! {num} kan ikke deles på 3')

    product *= num

print(f'Produktet av tallene {numbers} er {product}')