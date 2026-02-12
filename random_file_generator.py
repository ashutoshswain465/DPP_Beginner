import random
import string

length = 10
all_ch = string.ascii_letters + string.digits
filename = "".join(random.choices(all_ch, k=10))

with open(f"generated_file/{filename}", "w") as file:
    file.write(filename)

