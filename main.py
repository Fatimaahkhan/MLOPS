
import numpy as np

def main():
    print("Hello, World!")

# Define a function to calculate the area of a rectangle
def calculate_rectangle_area(length, width):
    area = length * width
    return area

def main():
    length = 5.0
    width = 3.0
    area = calculate_rectangle_area(length, width)
    print(f"The area of the rectangle with length {length} and width {width} is {area}.")

    # Example usage of numpy library
    data = [1, 2, 3, 4, 5]
    mean = np.mean(data)
    print(f"The mean of the data is: {mean}")

if __name__ == "__main__":
    main()
