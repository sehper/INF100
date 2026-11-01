from qr6_error_correction import generate_error_correction

def string_to_data(content_string):
    bits = []
    for character in content_string:
        for bit in format(ord(character), "08b"):
            bits.append(int(bit))
    return bits

def get_core_bit_list(content_string):
    mode = [0, 1, 0, 0]
    length = [int(bit) for bit in format(len(content_string), "08b")]
    data = string_to_data(content_string)
    terminator = [0, 0, 0, 0]
    return mode + length + data + terminator

def pad_bit_list(core_bit_list, pad_to_bytes):
    patterns = ([1, 1, 1, 0, 1, 1, 0, 0], [0, 0, 0, 1, 0, 0, 0, 1])
    target = 8 * pad_to_bytes
    index = 0
    while len(core_bit_list) < target:
        core_bit_list.extend(patterns[index % 2])
        index += 1
    return core_bit_list

def string_to_bit_list(content_string, qr_layout):
    capacity_bytes = qr_layout["byte_capacity"]
    ec_bytes = qr_layout["error_correction_bytes"]

    bit_list = get_core_bit_list(content_string)
    core_bytes = len(bit_list) // 8

    chosen_level = None
    for level in ("H", "Q", "M", "L"):
        if core_bytes + ec_bytes[level] <= capacity_bytes:
            chosen_level = level
            break

    if chosen_level is None:
        raise ValueError(
            f"Strengen er for lang: dataen trenger {core_bytes} bytes, "
            f"men det er bare plass til {capacity_bytes - ec_bytes['L']} bytes "
            f"med laveste feilrettingsnivå (L)."
        )

    pad_bit_list(bit_list, capacity_bytes - ec_bytes[chosen_level])
    full_bit_list = generate_error_correction(bit_list, chosen_level)
    return full_bit_list, chosen_level