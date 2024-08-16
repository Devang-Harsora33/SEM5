def calculate_parity_bits(data_bits):
    d = [int(bit) for bit in data_bits]
    
    p1 = (d[0] + d[1] + d[3]) % 2
    p2 = (d[0] + d[2] + d[3]) % 2
    p4 = (d[1] + d[2] + d[3]) % 2

    codeword = [p1, p2, d[0], p4, d[1], d[2], d[3]]
    
    return ''.join(map(str, codeword))

def encode_hamming(data_bits):
    if len(data_bits) != 4:
        raise ValueError("Data bits must be exactly 4 bits long")
    return calculate_parity_bits(data_bits)

def detect_and_correct(received_code):
    code = [int(bit) for bit in received_code]
    
    p1 = (code[0] + code[2] + code[4] + code[6]) % 2
    p2 = (code[1] + code[2] + code[5] + code[6]) % 2
    p4 = (code[3] + code[4] + code[5] + code[6]) % 2
    
    error_position = p1 * 1 + p2 * 2 + p4 * 4
    print("Error position: ",error_position+1)
    if error_position:
        if error_position <= len(code):
            code[error_position - 1] ^= 1  # Flip the bit to correct the error
    
    data_bits = code[2:3] + code[4:7]

    return ''.join(map(str, data_bits)), error_position

def hamming_sender(data_bits):
        return encode_hamming(data_bits)

def hamming_receiver(received_code):
    data_bits, error_position = detect_and_correct(received_code)
    if error_position:
        return f"Error detected and corrected. Data: {data_bits}"
    else:
        return f"No error detected. Data: {data_bits}"


data_bits = "1011"  

print("Original Data Bits:", data_bits)

# Sender side
encoded_code = hamming_sender(data_bits)
print("Encoded Hamming Code:", encoded_code)

received_code = list(encoded_code)
print("Receiving code: ", received_code)
received_code[2] = '1' if received_code[2] == '0' else '0'  # Introduce a bit error
print("Receiving code after changing: ", received_code)

received_code = ''.join(received_code)

# Receiver side
result = hamming_receiver(received_code)
print(result)
