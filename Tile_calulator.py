import math

# User inputs in meters and centimeters
width = float(input('Enter the room width (in meters): '))
length = float(input('Enter the room length (in meters): '))
edge = float(input('Enter the edge of a single piece (in centimeters): '))

# Convert room area from m² to cm²
room_area_cm2 = width * length * 10000

# Calculate area of one square piece in cm²
piece_area_cm2 = edge * edge

# Number of pieces needed (always round up)
num_pieces = room_area_cm2 / piece_area_cm2

print(f'\nYour room is {room_area_cm2:.2f} cm² and each piece is {piece_area_cm2:.2f} cm².')
print(f'You will need at least {math.ceil(num_pieces)} pieces.')
