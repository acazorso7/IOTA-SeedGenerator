import string
import random

def seed_generator(size, chars=string.ascii_uppercase + '9'):
    return ''.join(random.choice(chars) for _ in range(size))

def main():
    sequence = seed_generator(81)
    while('9' not in sequence):
        sequence = seed_generator(81)
        
    print "Your seed was generated. Check the file 'IOTA_seed.txt'"
    f = open('IOTA_seed.txt','w')
    f.write("**Never give this seed to anybody\n")
    f.write("**Keep your seed save, otherwise you might lose your IOTA.\n")
    f.write("**If you want to receive IOTA just generate an address in your wallet.\n\n")
    f.write("SEED: " +sequence)
    f.close()

main()
