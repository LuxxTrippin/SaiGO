import pyautogui
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import RectangleSelector

# Global variable to store coordinates
coords = []

def line_select_callback(eclick, erelease):
    """
    Callback function to get the starting and ending coordinates of the drawn rectangle.
    eclick and erelease are the mouse press and release events.
    """
    global coords
    x1, y1 = eclick.xdata, eclick.ydata
    x2, y2 = erelease.xdata, erelease.ydata
    coords = [(int(x1), int(y1)), (int(x2), int(y2))]

def get_screen_region():
    """
    Takes a screenshot and allows the user to draw a rectangle to select a region.
    Returns the left, top, width, and height of the selected region.
    """
    global coords
    
    # Take a screenshot using pyautogui
    screen = pyautogui.screenshot()

    # Convert the screenshot to a NumPy array (Pillow Image to NumPy)
    screen = np.array(screen)

    # Create a figure and axes for plotting the screenshot
    fig, ax = plt.subplots(1)
    ax.imshow(screen)

    # Create a rectangle selector widget
    rect_selector = RectangleSelector(
        ax, line_select_callback,
        interactive=True,  # For draggable/resizable behavior
        button=[1],  # Use left mouse button
        minspanx=5, minspany=5,  # Minimum size of the rectangle
        spancoords='pixels'
    )

    # Display the plot and wait for user input
    plt.show()

    if coords:
        # Calculate the left, top, width, and height
        (x1, y1), (x2, y2) = coords
        left = min(x1, x2)
        top = min(y1, y2)
        width = abs(x2 - x1)
        height = abs(y2 - y1)

        # Print the calculated values
        print(f"LEFT: {left}")
        print(f"TOP: {top}")
        print(f"WIDTH: {width}")
        print(f"HEIGHT: {height}")

        # Save the values to a notepad file
        with open("selected_region.txt", "w") as file:
            file.write(f"LEFT: {left}\n")
            file.write(f"TOP: {top}\n")
            file.write(f"WIDTH: {width}\n")
            file.write(f"HEIGHT: {height}\n")

        return left, top, width, height
    else:
        return None

# Use the function to get the selected region
region = get_screen_region()
if region:
    left, top, width, height = region
    # Take a screenshot of the specified region (optional)
    screenshot = pyautogui.screenshot(region=(left, top, width, height))
    screenshot.save("selected_region.png")  # Save the screenshot if needed
else:
    print("No region selected.")
