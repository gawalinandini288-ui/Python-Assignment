# ------------------------------------------------------------
# 6x6 Grayscale Image
# Top Half = Black (0)
# Bottom Half = White (255)
# Apply 3x3 Kernel for Edge Detection
# Show Feature Map
# ------------------------------------------------------------

import numpy as np

# ------------------------------------------------------------
# Step 1 : Create 6x6 Image
# ------------------------------------------------------------
image = np.array([
    [0,   0,   0,   0,   0],
    [0,   0,   0,   0,   0],
    [1,   1,   1,   1,   1],
    [0,   0,   0,   0,   0 ],
    [0,   0,   0,   0,   0]
])

print("\nOriginal 6x6 Image")
print(image)

# ------------------------------------------------------------
# Step 2 : 3x3 Kernel for Horizontal Edge Detection
# ------------------------------------------------------------
kernel = np.array([
    [-1, -1, -1],
    [ 0,  0,  0],
    [ 1,  1,  1]
])

print("\n3x3 Kernel")
print(kernel)

# ------------------------------------------------------------
# Step 3 : Convolution Operation
# Output Size = (5-3+1) x (5-3+1) = 3*3
# ------------------------------------------------------------
feature_map = np.zeros((3,3))

for i in range(3):
    for j in range(3):
        print("\n\n==================================================")
        print(f"Kernel Position -> Row: {i} to {i+2}, Column: {j} to {j+2}")
        print("==================================================")

        # Extract 3x3 region from image
        region = image[i:i+3, j:j+3]
        print("\nRegion:",region)

        # Element-wise multiplication
        multiplied = region * kernel
        print("\nMultiplication :",multiplied)
       

        # Sum all elements
        result = np.sum(multiplied)
        print("\nSum of all values =", result)

        # Store in feature map
        feature_map[i][j] = result

# ------------------------------------------------------------
# Step 4 : Show Feature Map
# ------------------------------------------------------------
print("\nFeature Map (Detected Edge)")
print(feature_map)

# ------------------------------------------------------------
# Step 5 : After Relu
# ------------------------------------------------------------

Relu = np.maximum(0,feature_map)
print("After Relu:\n",Relu)

# ------------------------------------------------------------
# Step 5 : Pooling
# ------------------------------------------------------------

rows , columns = Relu.shape

Output_rows = rows // 2
Output_columns = columns // 2

Output = np.zeros((Output_rows,Output_columns))

r = 0
for i in range(0,rows,2):
    c = 0
    for j in range(0,columns,2):
        Block = Relu[i:i+2 , j:j+2]
        
        if Block.shape != (2,2):
            continue
        max_value = np.max(Block)
        Output[r][c] = max_value

        print(f"\nPooling Block Position :Row : {r} column : {c}")
        print("\nSelected 2x2 Block :")
        print(Block)
        print("\nMaximum value selected = ",max_value)
        c += 1
    r += 1
print("\nFianl pooling Output :")
print(Output)


