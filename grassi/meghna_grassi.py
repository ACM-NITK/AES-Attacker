# S-box
sbox = [0x63, 0x7c, 0x77, 0x7b, 0xf2, 0x6b, 0x6f, 0xc5, 0x30, 0x01, 0x67,
        0x2b, 0xfe, 0xd7, 0xab, 0x76, 0xca, 0x82, 0xc9, 0x7d, 0xfa, 0x59,
        0x47, 0xf0, 0xad, 0xd4, 0xa2, 0xaf, 0x9c, 0xa4, 0x72, 0xc0, 0xb7,
        0xfd, 0x93, 0x26, 0x36, 0x3f, 0xf7, 0xcc, 0x34, 0xa5, 0xe5, 0xf1,
        0x71, 0xd8, 0x31, 0x15, 0x04, 0xc7, 0x23, 0xc3, 0x18, 0x96, 0x05,
        0x9a, 0x07, 0x12, 0x80, 0xe2, 0xeb, 0x27, 0xb2, 0x75, 0x09, 0x83,
        0x2c, 0x1a, 0x1b, 0x6e, 0x5a, 0xa0, 0x52, 0x3b, 0xd6, 0xb3, 0x29,
        0xe3, 0x2f, 0x84, 0x53, 0xd1, 0x00, 0xed, 0x20, 0xfc, 0xb1, 0x5b,
        0x6a, 0xcb, 0xbe, 0x39, 0x4a, 0x4c, 0x58, 0xcf, 0xd0, 0xef, 0xaa,
        0xfb, 0x43, 0x4d, 0x33, 0x85, 0x45, 0xf9, 0x02, 0x7f, 0x50, 0x3c,
        0x9f, 0xa8, 0x51, 0xa3, 0x40, 0x8f, 0x92, 0x9d, 0x38, 0xf5, 0xbc,
        0xb6, 0xda, 0x21, 0x10, 0xff, 0xf3, 0xd2, 0xcd, 0x0c, 0x13, 0xec,
        0x5f, 0x97, 0x44, 0x17, 0xc4, 0xa7, 0x7e, 0x3d, 0x64, 0x5d, 0x19,
        0x73, 0x60, 0x81, 0x4f, 0xdc, 0x22, 0x2a, 0x90, 0x88, 0x46, 0xee,
        0xb8, 0x14, 0xde, 0x5e, 0x0b, 0xdb, 0xe0, 0x32, 0x3a, 0x0a, 0x49,
        0x06, 0x24, 0x5c, 0xc2, 0xd3, 0xac, 0x62, 0x91, 0x95, 0xe4, 0x79,
        0xe7, 0xc8, 0x37, 0x6d, 0x8d, 0xd5, 0x4e, 0xa9, 0x6c, 0x56, 0xf4,
        0xea, 0x65, 0x7a, 0xae, 0x08, 0xba, 0x78, 0x25, 0x2e, 0x1c, 0xa6,
        0xb4, 0xc6, 0xe8, 0xdd, 0x74, 0x1f, 0x4b, 0xbd, 0x8b, 0x8a, 0x70,
        0x3e, 0xb5, 0x66, 0x48, 0x03, 0xf6, 0x0e, 0x61, 0x35, 0x57, 0xb9,
        0x86, 0xc1, 0x1d, 0x9e, 0xe1, 0xf8, 0x98, 0x11, 0x69, 0xd9, 0x8e,
        0x94, 0x9b, 0x1e, 0x87, 0xe9, 0xce, 0x55, 0x28, 0xdf, 0x8c, 0xa1,
        0x89, 0x0d, 0xbf, 0xe6, 0x42, 0x68, 0x41, 0x99, 0x2d, 0x0f, 0xb0,
        0x54, 0xbb, 0x16]

Rcon = [0x8d, 0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1b, 0x36,
        0x6c, 0xd8, 0xab, 0x4d, 0x9a, 0x2f, 0x5e, 0xbc, 0x63, 0xc6, 0x97,
        0x35, 0x6a, 0xd4, 0xb3, 0x7d, 0xfa, 0xef, 0xc5, 0x91, 0x39, 0x72,
        0xe4, 0xd3, 0xbd, 0x61, 0xc2, 0x9f, 0x25, 0x4a, 0x94, 0x33, 0x66,
        0xcc, 0x83, 0x1d, 0x3a, 0x74, 0xe8, 0xcb, 0x8d, 0x01, 0x02, 0x04,
        0x08, 0x10, 0x20, 0x40, 0x80, 0x1b, 0x36, 0x6c, 0xd8, 0xab, 0x4d,
        0x9a, 0x2f, 0x5e, 0xbc, 0x63, 0xc6, 0x97, 0x35, 0x6a, 0xd4, 0xb3,
        0x7d, 0xfa, 0xef, 0xc5, 0x91, 0x39, 0x72, 0xe4, 0xd3, 0xbd, 0x61,
        0xc2, 0x9f, 0x25, 0x4a, 0x94, 0x33, 0x66, 0xcc, 0x83, 0x1d, 0x3a,
        0x74, 0xe8, 0xcb, 0x8d, 0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40,
        0x80, 0x1b, 0x36, 0x6c, 0xd8, 0xab, 0x4d, 0x9a, 0x2f, 0x5e, 0xbc,
        0x63, 0xc6, 0x97, 0x35, 0x6a, 0xd4, 0xb3, 0x7d, 0xfa, 0xef, 0xc5,
        0x91, 0x39, 0x72, 0xe4, 0xd3, 0xbd, 0x61, 0xc2, 0x9f, 0x25, 0x4a,
        0x94, 0x33, 0x66, 0xcc, 0x83, 0x1d, 0x3a, 0x74, 0xe8, 0xcb, 0x8d,
        0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1b, 0x36, 0x6c,
        0xd8, 0xab, 0x4d, 0x9a, 0x2f, 0x5e, 0xbc, 0x63, 0xc6, 0x97, 0x35,
        0x6a, 0xd4, 0xb3, 0x7d, 0xfa, 0xef, 0xc5, 0x91, 0x39, 0x72, 0xe4,
        0xd3, 0xbd, 0x61, 0xc2, 0x9f, 0x25, 0x4a, 0x94, 0x33, 0x66, 0xcc,
        0x83, 0x1d, 0x3a, 0x74, 0xe8, 0xcb, 0x8d, 0x01, 0x02, 0x04, 0x08,
        0x10, 0x20, 0x40, 0x80, 0x1b, 0x36, 0x6c, 0xd8, 0xab, 0x4d, 0x9a,
        0x2f, 0x5e, 0xbc, 0x63, 0xc6, 0x97, 0x35, 0x6a, 0xd4, 0xb3, 0x7d,
        0xfa, 0xef, 0xc5, 0x91, 0x39, 0x72, 0xe4, 0xd3, 0xbd, 0x61, 0xc2,
        0x9f, 0x25, 0x4a, 0x94, 0x33, 0x66, 0xcc, 0x83, 0x1d, 0x3a, 0x74,
        0xe8, 0xcb]

fixed_matrix = [[0x02, 0x03, 0x01, 0x01],[0x01, 0x02, 0x03, 0x01],[0x01, 0x01, 0x02, 0x03],[0x03, 0x01, 0x01, 0x02]]

def get_roundkeys(x):
  #first round key
    keys = [[] for _ in range(44)]
    
    for i in range(16):
          byte = (x >> ( 8 * (15- i ))) & int(0xff)
          keys[int(i / 4)].append(byte)
    #print(keys)
  #rest of the round keys
    for i in range(4,44):
        temp=keys[i-1]
        if i%4==0:
            rot=[]
            rot.append(keys[i-1][1])
            rot.append(keys[i-1][2])
            rot.append(keys[i-1][3])
            rot.append(keys[i-1][0])
            for j in range(4):
              if j==0:
                  byte=sbox[rot[j]] ^ Rcon[int(i/4)]
              else:
                  byte=sbox[rot[j]]
              keys[i].append(byte ^ keys[i-4][j])
        else:
            for j in range(4):
                keys[i].append(keys[i-4][j]^keys[i-1][j])
    #print(keys)    
    return keys

def key_to_state(key_no,keys):
        key = [[] for _ in range(4)]
        for i in range(4):
            for j in range(4):
                key[i].append(keys[key_no+j][i])
        return key

def text_to_state(text):
    matrix = [[] for _ in range(4)]
    
    for i in range(16):
          byte = (text >> ( 8 * (15- i ))) & 0xff
          matrix[int(i / 4)].append(byte)
    matrix2 = [[] for _ in range(4)]
    for i in range(4):
        for j in range(4):
            matrix2[i].append(matrix[j][i])      
    
    return matrix2

def state_to_text(matrix):
    text = 0
    for i in range(4):
        for j in range(4):
            text |= (matrix[j][i] << (120 - 8 * (4 * i + j)))
    #print(text)
    return text

def encrypt(key,matrix):
    keys = get_roundkeys(key)
    
    #adding round 0 key 
    cipher = [[[] for __ in range(4) ] for _ in range(11)]
    key0 = key_to_state(0,keys)
    
    for i in range(4):
        for j in range(4):
            cipher[0][i].append(key0[i][j] ^ matrix[i][j])
    
    #rounds 1-4
    for i in range(1,5):
      
        #substitution
        sbox_state = [[] for _ in range(4)]
        for j in range(4):
            for k in range(4):
                sbox_state[j].append(sbox[cipher[i-1][j][k]])
        #print(sbox_state)
        
        #shift rows
        shiftrow_state = [[] for _ in range(4)]
        for j in range(4):
            for k in range(4):
                shiftrow_state[j].append(sbox_state[j][(k+j)%4])
        #print(shiftrow_state)
        
        #mix columns
        mixcol_state = [[] for _ in range(4)]
        for j in range(4):
            for k in range(4):
                sum=0
                for l in range(4):
                    if fixed_matrix[j][l] == 0x01:
                        sum = sum ^ shiftrow_state[l][k]
                    elif fixed_matrix[j][l] == 0x02:
                        if shiftrow_state[l][k]>127:
                            sum = sum ^ (((shiftrow_state[l][k]<<1)-256)^0x1b)
                        else:
                            sum = sum ^ ((shiftrow_state[l][k]<<1))
                    elif fixed_matrix[j][l] == 0x03:
                        if shiftrow_state[l][k]>127:
                            sum = sum ^ ((((shiftrow_state[l][k]<<1)-256)^0x1b)  ^ shiftrow_state[l][k])
                        else:
                            sum = sum ^ (((shiftrow_state[l][k]<<1)) ^ shiftrow_state[l][k])
                    #print(sum)
                mixcol_state[j].append(sum)
        #print(mixcol_state)
                
        #add roundkey
        roundkey = key_to_state(i*4,keys)  
        for j in range(4):
            for k in range(4):
                cipher[i][j].append(roundkey[j][k] ^ mixcol_state[j][k])
        #print(cipher[i])
        
    #round 5 
    
    #substitution
        
    sbox_state = [[] for _ in range(4)]
    for j in range(4):
        for k in range(4):
            sbox_state[j].append(sbox[cipher[4][j][k]])
    #print(sbox_state)

    #shift rows
    shiftrow_state = [[] for _ in range(4)]
    for j in range(4):
        for k in range(4):
            shiftrow_state[j].append(sbox_state[j][(k+j)%4])
    #print(shiftrow_state)
    
    #add roundkey
    roundkey = key_to_state(10*4,keys)  
    for j in range(4):
        for k in range(4):
            cipher[5][j].append(roundkey[j][k] ^ shiftrow_state[j][k])
    return cipher[5]

    
    #adding round 0 key
    cipher = [[[] for __ in range(4) ] for _ in range(11)]
    key0 = key_to_state(0,keys)
    
    for i in range(4):
        for j in range(4):
            cipher[0][i].append(key0[i][j] ^ matrix[i][j])
    
    #round 1
    for i in range(1,2):
        #substitution
        sbox_state = [[] for _ in range(4)]
        for j in range(4):
            for k in range(4):
                sbox_state[j].append(sbox[cipher[i-1][j][k]])
        
        #shift rows
        shiftrow_state = [[] for _ in range(4)]
        for j in range(4):
            for k in range(4):
                shiftrow_state[j].append(sbox_state[j][(k+j)%4])
        
        #mix columns
        mixcol_state = [[] for _ in range(4)]
        for j in range(4):
            for k in range(4):
                sum=0
                for l in range(4):
                    if fixed_matrix[j][l] == 0x01:
                        sum = sum ^ shiftrow_state[l][k]
                    elif fixed_matrix[j][l] == 0x02:
                        if shiftrow_state[l][k]>127:
                            sum = sum ^ (((shiftrow_state[l][k]<<1)-256)^0x1b)
                        else:
                            sum = sum ^ ((shiftrow_state[l][k]<<1))
                    elif fixed_matrix[j][l] == 0x03:
                        if shiftrow_state[l][k]>127:
                            sum = sum ^ ((((shiftrow_state[l][k]<<1)-256)^0x1b)  ^ shiftrow_state[l][k])
                        else:
                            sum = sum ^ (((shiftrow_state[l][k]<<1)) ^ shiftrow_state[l][k])
                mixcol_state[j].append(sum)
                
        #add roundkey
        roundkey = key_to_state(i*4,keys)  
        for j in range(4):
            for k in range(4):
                cipher[i][j].append(roundkey[j][k] ^ mixcol_state[j][k])
    #return cipher[1]

def encrypt_rounds(key,matrix):
    keys = get_roundkeys(key)
    
    #adding round 0 key
    cipher = [[[] for __ in range(4) ] for _ in range(11)]
    key0 = key_to_state(0,keys)
    
    for i in range(4):
        for j in range(4):
            cipher[0][i].append(key0[i][j] ^ matrix[i][j])
    
    #round 2,3,4
    for i in range(2,5):
        #substitution
        sbox_state = [[] for _ in range(4)]
        for j in range(4):
            for k in range(4):
                sbox_state[j].append(sbox[cipher[i-1][j][k]])
        
        #shift rows
        shiftrow_state = [[] for _ in range(4)]
        for j in range(4):
            for k in range(4):
                shiftrow_state[j].append(sbox_state[j][(k+j)%4])
        
        #mix columns
        mixcol_state = [[] for _ in range(4)]
        for j in range(4):
            for k in range(4):
                sum=0
                for l in range(4):
                    if fixed_matrix[j][l] == 0x01:
                        sum = sum ^ shiftrow_state[l][k]
                    elif fixed_matrix[j][l] == 0x02:
                        if shiftrow_state[l][k]>127:
                            sum = sum ^ (((shiftrow_state[l][k]<<1)-256)^0x1b)
                        else:
                            sum = sum ^ ((shiftrow_state[l][k]<<1))
                    elif fixed_matrix[j][l] == 0x03:
                        if shiftrow_state[l][k]>127:
                            sum = sum ^ ((((shiftrow_state[l][k]<<1)-256)^0x1b)  ^ shiftrow_state[l][k])
                        else:
                            sum = sum ^ (((shiftrow_state[l][k]<<1)) ^ shiftrow_state[l][k])
                mixcol_state[j].append(sum)
                
        #add roundkey
        roundkey = key_to_state(i*4,keys)  
        for j in range(4):
            for k in range(4):
                cipher[i][j].append(roundkey[j][k] ^ mixcol_state[j][k])
      #round 5 
    
    #substitution
        
    sbox_state = [[] for _ in range(4)]
    for j in range(4):
        for k in range(4):
            sbox_state[j].append(sbox[cipher[4][j][k]])

    #shift rows
    shiftrow_state = [[] for _ in range(4)]
    for j in range(4):
        for k in range(4):
            shiftrow_state[j].append(sbox_state[j][(k+j)%4])
    #add roundkey
    roundkey = key_to_state(10*4,keys)  
    for j in range(4):
        for k in range(4):
            cipher[5][j].append(roundkey[j][k] ^ shiftrow_state[j][k])
    print(cipher[5])
    return cipher[5]

def encrypt0_1(key,matrix):

    keys = get_roundkeys(key)
    
    #adding round 0 key
    cipher = [[[] for __ in range(4) ] for _ in range(11)]
    key0 = key_to_state(0,keys)
    
    for i in range(4):
        for j in range(4):
            cipher[0][i].append(key0[i][j] ^ matrix[i][j])
    
    #round 1
    for i in range(1,2):
        #substitution
        sbox_state = [[] for _ in range(4)]
        for j in range(4):
            for k in range(4):
                sbox_state[j].append(sbox[cipher[i-1][j][k]])
        
        #shift rows
        shiftrow_state = [[] for _ in range(4)]
        for j in range(4):
            for k in range(4):
                shiftrow_state[j].append(sbox_state[j][(k+j)%4])
        
        #mix columns
        mixcol_state = [[] for _ in range(4)]
        for j in range(4):
            for k in range(4):
                sum=0
                for l in range(4):
                    if fixed_matrix[j][l] == 0x01:
                        sum = sum ^ shiftrow_state[l][k]
                    elif fixed_matrix[j][l] == 0x02:
                        if shiftrow_state[l][k]>127:
                            sum = sum ^ (((shiftrow_state[l][k]<<1)-256)^0x1b)
                        else:
                            sum = sum ^ ((shiftrow_state[l][k]<<1))
                    elif fixed_matrix[j][l] == 0x03:
                        if shiftrow_state[l][k]>127:
                            sum = sum ^ ((((shiftrow_state[l][k]<<1)-256)^0x1b)  ^ shiftrow_state[l][k])
                        else:
                            sum = sum ^ (((shiftrow_state[l][k]<<1)) ^ shiftrow_state[l][k])
                mixcol_state[j].append(sum)
                
        #add roundkey
        roundkey = key_to_state(i*4,keys)  
        for j in range(4):
            for k in range(4):
                cipher[i][j].append(roundkey[j][k] ^ mixcol_state[j][k])
    print(cipher[1])
    return cipher[1]


def good_pair(key):
    plain1 = [[0,0,0,0] for _ in range(4)]
    plain2 = [[0,0,0,0] for _ in range(4)]
    for i1 in range(256):
        for j1 in range(256):
            for k1 in range(256):
                for l1 in range(256):
                    for i2 in range(256):
                        for j2 in range(256):
                            for k2 in range(256):
                                for l2 in range(256):
                                    plain2[0][0]=l1
                                    plain2[1][1]=k1
                                    plain2[2][2]=j1
                                    plain2[3][3]=i1
                                    plain1[0][0]=l2
                                    plain1[1][1]=k2
                                    plain1[2][2]=j2
                                    plain1[3][3]=i2
                                    p1_encrypt = encrypt(key,plain2)
                                    p2_encrypt = encrypt(key,plain1)
                                    if(p2[0][0]==p1[0][0] and p2[1][3]==p1[1][3] and p2[2][2]==p1[2][2] and p2[3][1]==p1[3][1] and p2!=p1):
                                        print(p1_encrypt)
                                        print(p2_encrypt)
                                        return(p1_encrypt,p2_encrypt)

key = "2b7e151628aed2a6abf7158809cf4f3c"
p1,p2=good_pair(key)

def find_key(p1,p2):
    key_trial = [[0,0,0,0] for _ in range(4)]
    for i in range(256):
        for j in range(256):
            for k in range(256):
                for l in range(256):
                    key_trial[0][0]=l
                    key_trial[1][1]=k
                    key_trial[2][2]=j
                    key_trial[3][3]=i
                    x1=encrypt0_1(key_try,gp1)	
                    y1=encrypt0_1(key_try,gp2)
                    z1=x1
                    w1=y1
                    w1[1][0]=x1[1][0]
                    z1[1][0]=y1[1][0]
                    w1[3][0]=x1[1][0]
                    z1[3][0]=y1[3][0]
                    encrypt1=encrypt_rounds(key_trial,z1)
                    encrypt2=encrypt_rounds(key_trial,w1)
                    if(encrypt1[0][0]==encrypt2[0][0] and encrypt1[1][3]==encrypt2[1][3] and encrypt1[2][2]==encrypt2[2][2] and encrypt1[3][1]==encrypt2[3][1]):
                      print("Working")
                      print(key_trial)


find_key(p1,p2)

            
        




