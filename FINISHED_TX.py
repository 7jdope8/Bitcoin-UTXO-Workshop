from ecc import PrivateKey
from helper import decode_base58, little_endian_to_int, hash256
from script import p2pkh_script
from tx import TxIn, TxOut, Tx

#PRIVATE  KEY
SEMILLA = b'HolaHashgerTraines'
SECRETO = little_endian_to_int(hash256(SEMILLA)) 
PrivKey = PrivateKey(SECRETO)
print('Mi llave privada es: ',PrivKey.hex())
ADDRESS = PrivKey.point.address(testnet=True)
print('Mi direecion  Bitcoin testenet es: ', ADDRESS)

#INPUTS
tx_previa = bytes.fromhex('b685879f3939fa9531899b729394ed85edab8b6850b72a9e378ea31af96a304a')
index_tx_previa = 1

tx_inputs = []
tx_inputs.append(TxIn(tx_previa, index_tx_previa))

#OUPUTS
tx_outputs = []
destinatario = 'mv4rnyY3Su5gjcDNzbMLKBQkBicCtHUtFB'
monto = .00008
change_adress = ADDRESS
cambio = .00001
#SEND OUTPUT
h160 = decode_base58(destinatario)
script_pubkey = p2pkh_script(h160)
monto_satoshis = int(monto * 100_000_000)
tx_outputs.append(TxOut(monto_satoshis, script_pubkey))

#CHANGE OUPUT
h160 = decode_base58(change_adress)
script_pubkey = p2pkh_script(h160)
cambio_satoshis = int(cambio * 100_000_000)
tx_outputs.append(TxOut(cambio_satoshis, script_pubkey))

#TX BUILD
TX_BUILD = Tx(1,tx_inputs, tx_outputs, 0, testnet=True)

#SIGN
print(TX_BUILD.sign_input(0, PrivKey))
print(TX_BUILD.serialize().hex())
