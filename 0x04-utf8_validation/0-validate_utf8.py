#!/usr/bin/python3
""" UTF-8 Validation """


def validUTF8(data):
    """
    Method that determines if a given data set represents a valid
    UTF-8 encoding.
    """
    bytes_remaining = 0

    mask_1 = 1 << 7
    mask_2 = 1 << 6

    for num in data:

        mask_byte = 1 << 7

        if bytes_remaining == 0:

            while mask_byte & num:
                bytes_remaining += 1
                mask_byte = mask_byte >> 1

            if bytes_remaining == 0:
                continue

            if bytes_remaining == 1 or bytes_remaining > 4:
                return False

        else:
            if not (num & mask_1 and not (num & mask_2)):
                    return False

        bytes_remaining -= 1

    if bytes_remaining == 0:
        return True

    return False
