from ecc import PrivateKey
from helper import decode_base58, little_endian_to_int, hash256
from script import p2pkh_script, Script
from tx import TxIn, TxOut, Tx


SEMILLA = b'HolaHashgerTraines'
SECRETO = little_endian_to_int(hash256(SEMILLA)) 
PrivKey = PrivateKey(SECRETO)

print('Mi direecion  Bitcoin testenet es: ',PrivKey.point.address(testnet=True))