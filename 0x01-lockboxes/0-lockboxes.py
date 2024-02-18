def canUnlockAll(boxes):
    # Set to keep track of opened boxes
    opened_boxes = set()

    # Initially, the first box is open
    opened_boxes.add(0)

    # List to keep track of keys obtained
    keys_to_obtain = [0]

    # Iterate through the keys and try to open boxes
    while keys_to_obtain:
        current_key = keys_to_obtain.pop()

        # Iterate through the keys found in the current box
        for key in boxes[current_key]:
            # If the key opens a new box and it is not opened yet
            if key not in opened_boxes and key < len(boxes):
                opened_boxes.add(key)
                keys_to_obtain.append(key)

    # Check if all boxes are opened
    return len(opened_boxes) == len(boxes)
