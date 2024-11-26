def crc(data, divisor):
    n = len(divisor)
    temp = data + '0' * (n - 1)  # Append zeros 
    temp = list(temp)
    divisor = list(divisor)
    for i in range(len(data)):
        if temp[i] == '1':
            for j in range(n):
                temp[i + j] = str(int(temp[i + j]) ^ int(divisor[j]))
    
    remainder = ''.join(temp[-(n - 1):]) 
    return remainder

def crc2(received_data, divisor):
    n = len(divisor)
    temp = list(received_data)  # Dont append zeros
    divisor = list(divisor)
    for i in range(len(received_data) - n + 1):
        if temp[i] == '1':
            for j in range(n):
                temp[i + j] = str(int(temp[i + j]) ^ int(divisor[j]))
    
    remainder = ''.join(temp[-(n - 1):]) 
    return remainder
#both are same functions except for appending zeros part
def flip_bit(data, position):
    data = list(data)
    data[position] = '1' if data[position] == '0' else '0'
    return ''.join(data)

#Sender Side
data = input("Enter data to be sent: ")
key = input("Enter key: ")

checksum = crc(data, key)
sent_data = data + checksum
print(f"Sent data: {sent_data}")

#Receiver side
received_data = input("Enter received data: ")
remainder = crc2(received_data, key)

if int(remainder) == 0:
    print("Data received without errors.")
else:
    print(f"Error detected in received data. Remainder: {remainder}")

    error_position = int(remainder, 2)  # Convert binary remainder to decimal
    print(f"Error detected at bit position (0-based): {error_position}")
    
    # Flip the erroneous bit
    corrected_data = flip_bit(received_data, error_position)
    print(f"Corrected data: {corrected_data}")
    
    # Recheck the corrected data
    new_remainder = crc2(corrected_data, key)
    if int(new_remainder) == 0:
        print("Data correction successful. No errors in corrected data.")
    else:
        print(f"Correction failed. New remainder: {new_remainder}")