# --------------
##File path for the file 
file_path 

#Code starts here
def read_file(path):
    fp = open(file_path, 'r')
    sentence = str(fp.readline())
    fp.close()
    return sentence
sample_message = str(read_file(file_path))

print(sample_message)


# --------------
#Code starts here
f1 = file_path_1
f2 = file_path_2
message_1 = read_file(f1)
message_2 = read_file(f2)
print(type(message_1))
print(message_1)
print(message_2)

def fuse_msg(message_a,message_b):
    quotient = int(message_b)//int(message_a)
    return str(quotient)
secret_msg_1 = fuse_msg(message_1,message_2)


# --------------
#Code starts here
message_3 = read_file(file_path_3)
print(message_3)

def substitute_msg(message_c):
    if(message_c == "Red"):
        return 'Army General'
    elif(message_c == "Green"):
        return 'Data Scientist'
    else:
        return 'Marine Biologist'
    # di = {'Red':'Army General','Green':'Data Scientist', 'Blue':'Marine Biologist'}
secret_msg_2 = str(substitute_msg(message_3))


# --------------
# File path for message 4  and message 5
file_path_4
file_path_5

#Code starts here
message_4 = read_file(file_path_4)
message_5 = read_file(file_path_5)
print(message_4)
print(message_5)

def compare_msg(message_d,message_e):
    a_list = message_d.split()
    b_list = message_e.split()
    c_list = [x for x in a_list if x not in b_list]
    final_msg = " ".join(c_list)
    return str(final_msg)
secret_msg_3 = compare_msg(message_4,message_5)







# --------------
#Code starts here
file_path_6
message_6 = str(read_file(file_path_6))
print(message_6)

def extract_msg(message_f):
    a_list = message_f.split()
    even_word = lambda y: len(y)%2==0
    b_list = list(filter(even_word, a_list))
    final_msg = " ".join(b_list)
    return final_msg

secret_msg_4 = extract_msg(message_6)


# --------------
#Secret message parts in the correct order
message_parts=[secret_msg_3, secret_msg_1, secret_msg_4, secret_msg_2]


final_path= user_data_dir + '/secret_message.txt'

#Code starts here
secret_msg = ' '.join(message_parts)
def write_file(secret_msg ,path):
    tmp = open(path, 'a+')
    tmp.write(secret_msg)
    tmp.close()

print(secret_msg)


