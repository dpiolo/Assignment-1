def calculate_max_height(initial_velocity, gravity):
    time_to_max_height = initial_velocity / gravity  # Time taken to reach maximum height
    max_height = (initial_velocity ** 2) / (2 * gravity)  # Maximum height formula
    return max_height

# Input initial velocity and gravity in ft/s
initial_velocity = float(input("Enter the initial velocity (ft/s): "))
gravity = 32.8  # ft/s^2

max_height = calculate_max_height(initial_velocity, gravity)
print(f"The maximum height of the projectile is {max_height} feet.")
