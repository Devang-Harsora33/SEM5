def append_crc(sender_data, sender_key):
    key_length = len(sender_key) - 1
    extended_data = sender_data + '0' * key_length

    dividend = int(extended_data, 2)
    divisor = int(sender_key, 2)

    remainder = dividend % divisor

    remainder_binary = bin(remainder)[2:].zfill(key_length)

    final_data = sender_data + remainder_binary
    return final_data

def error_detection(receiver_data, receiver_key):
    key_length = len(receiver_key) - 1
    divisor = int(receiver_key, 2)
    dividend = int(receiver_data, 2)

    remainder = dividend % divisor

    remainder_binary = bin(remainder)[2:].zfill(key_length)

    if remainder == 0:
        return f"There is no error in the file and the result was: {remainder}"
    else:
        return f"There is an error in the file and the result was: {remainder}"

# Example usage:
data = "100100"
key = "1101"

print("Data:", data)
print("Key:", key)


final_data = append_crc(data, key)
print("Data with CRC appended:", final_data)


result = error_detection(final_data, data)
print(result)
