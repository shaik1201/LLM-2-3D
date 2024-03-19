import rhinoscriptsyntax as rs

def create_box():
    # Prompt the user to specify the base plane for the box
    base_plane = rs.GetPlaneObject("Select the base plane for the box")
    if not base_plane:
        return  # User canceled the operation

    # Prompt the user to specify the dimensions of the box
    length = rs.GetReal("Length of the box", 10)
    width = rs.GetReal("Width of the box", 10)
    height = rs.GetReal("Height of the box", 10)
    
    if length is None or width is None or height is None:
        return  # User canceled the operation

    # Create the box
    box = rs.AddBox(base_plane, length, width, height)
    if box:
        print("Box created successfully.")
    else:
        print("Failed to create box.")

# Call the function to create the box
create_box()
