frame = []
processedFrame = []

frameLen = int(input("Enter the length of the frame: "))
newLen = frameLen + 1

for i in range(frameLen):
    framechar = input("Enter the character: ")
    frame.append(framechar)

frame_str = ''.join(frame)

processed_str = frame_str.replace('01111110', '011111010')

processedFrame.append("0111110")
processedFrame.append(processed_str)
processedFrame.append("01111110")

processedFrame_str = ' '.join(processedFrame)

print(processedFrame_str)