import os
import random
from PIL import Image, ImageOps

# Read the list of Pokemon names from the pokemon.txt file
pokemon_names=[]
with open('pokemon.txt', 'r', encoding="utf-8") as f:
    for line in f:
        pokemon_names.append(line.strip())
i = 1
# Loop over each Pokemon name and create a sub-folder for it in the Pokemon directory
for pokemon_name in pokemon_names:
    print(i,pokemon_name)
    pokemon_dir = os.path.join('Pokemon', pokemon_name)
    os.makedirs(pokemon_dir, exist_ok=True)
    
    image_path = os.path.join('data', f'{i}.png')
    image = Image.open(image_path).resize((236,236)).convert("RGBA")
    
    # Create five copies of the image with different color backgrounds
    for j in range(1, 6):
        # Create a new image with random background color
        background_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        new_image = Image.new('RGB', (400, 250), color=background_color)
            
        # Reduce the dimensions of the Pokemon image by a random amount between 2% and 10%
        size_percent = random.uniform(0.05, 0.2)
        new_width = int(image.width * (1 - size_percent))
        new_height = int(image.height * (1 - size_percent))
        pokemon_image = image.resize((new_width, new_height)).convert("RGBA")
        
        # Calculate the maximum x and y offsets that will keep the Pokemon image within the bounds of the new image
        max_x_offset = 400 - new_width
        max_y_offset = 250 - new_height
        
        # Generate random x and y offsets within the bounds of the new image
        x_offset = random.randint(0, max_x_offset)
        y_offset = random.randint(0, max_y_offset)
        
        # Ensure that the x and y offsets are within the bounds of the new image
        x_offset = min(max(x_offset, 0), max_x_offset)
        y_offset = min(max(y_offset, 0), max_y_offset)
        
        # Paste the Pokemon image in the new location
        new_image.paste(pokemon_image, (x_offset, y_offset), mask=pokemon_image)
        
        # Save the copy in the sub-folder with the appropriate name
        copy_path = os.path.join(pokemon_dir, f'{j}.png')
        new_image.save(copy_path)
    
        # Create five more copies with mirrored images
    for j in range(6, 11):
        # Create a new image with random background color
        background_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        new_image = Image.new('RGB', (400, 250), color=background_color)

        # Reduce the dimensions of the Pokemon image by a random amount between 2% and 10%
        size_percent = random.uniform(0.05, 0.2)
        new_width = int(image.width * (1 - size_percent))
        new_height = int(image.height * (1 - size_percent))
        pokemon_image = image.resize((new_width, new_height)).convert("RGBA")

        # Flip the Pokemon image horizontally and paste it in the new image
        flipped_pokemon = pokemon_image.transpose(method=Image.FLIP_LEFT_RIGHT)
        new_image.paste(flipped_pokemon, (x_offset, y_offset), mask=flipped_pokemon)

        # Save the copy in the sub-folder with the appropriate name
        copy_path = os.path.join(pokemon_dir, f'{j}.jpg')
        new_image.save(copy_path)
    i+=1
print("All copies created successfully!")

