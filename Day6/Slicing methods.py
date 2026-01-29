# slicing methods in python
#Positive indexing in slicing
Message = "Linux is an open-source operating system."
print(Message[0:6]) #index 0 to 5
print(Message[9: ]) #index 9 to end
print(Message[0: ]) #full string
print(Message[ :9]) #index 0 to 8
print(Message[5:12]) #index 5 to 11
#Negative indexing in slicing
print(Message[-7: ]) #index -7 to end
print(Message[-3:-1]) #index -3 to -2
#Step value in slicing
print(Message[0::2]) #even index characters
print(Message[::3]) #every 3rd character
print(Message[0:20:4]) #index 0 to 19 with step value 4
#Reversing a string using slicing
print(Message[::-1]) #normal reverse
print(Message[0::-1]) #reverse from index 0
print(Message[0::-4])  #reverse with step value
print(Message[20:0:-2]) #reverse from index 20 to 0 with step value