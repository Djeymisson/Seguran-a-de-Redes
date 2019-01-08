from random import randint

p = 17
q = 23

n = 0
phi_n = 0

e = 0
d = -1

msg = 'fofinho'
msg_enc = []
msg_dec = []

def get_mdc(a, b):
    return a if not b else get_mdc(b, a % b)

def modinv(A, M):
    for i in xrange(0, M):
        if (A*i) % M == 1:
            return i
    return -1

def iniatilize():
	global n, phi_n, e, d
	
	n = p*q
	phi_n = (p-1)*(q-1)

	mdc = 0
	while mdc != 1 or d == -1:
		e = randint(1, phi_n-1)
		mdc = get_mdc(e, phi_n)
		d = modinv(e, phi_n)

def encryptate():
	global msg, msg_enc, n, e

	msg_ascii = [ord(c) for c in msg]
	msg_enc = [pow(int(x), e, n) for x in msg_ascii]

	print 'msg enc', msg_enc

def decryptate():
	global msg_enc, n, d

	msg_dec = [pow(int(x), d, n) for x in msg_enc]
	msg_ascii = [chr(c) for c in msg_dec]

	print 'msg text =',''.join(msg_ascii)

def main():
	iniatilize()
	print 'n = {}, phi_n = {}, e = {}, d = {}'.format(n, phi_n, e, d)

	encryptate()
	decryptate()

main()