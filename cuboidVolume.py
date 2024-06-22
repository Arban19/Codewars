def Vol_cuboid(length,breadth,height):
    return length*breadth*height
    
length = int(input("What is the length of the cuboid? "))
breadth = int(input("What is the breadth of the cuboid? "))
height = int(input("What is the height of the cuboid? "))
vol = Vol_cuboid(length,breadth,height)
print("Volume of the cuboid is " + str(vol) + " units cubed.")
