import time


def base10_to_base36(number, alphabet='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
    """Converts an integer to a base36 string."""
    if not isinstance(number, (int, long)):
        raise TypeError('number must be an integer')

    base36 = ''
    sign = ''

    if number < 0:
        sign = '-'
        number = -number

    if 0 <= number < len(alphabet):
        return sign + alphabet[number]

    while number != 0:
        number, i = divmod(number, len(alphabet))
        base36 = alphabet[i] + base36

    return sign + base36


def base36_to_base10(number):
    return int(number, 36)


def encode(timestamp, mod_scalar=36893488147419103239,
           mod=100000000000000000000):
    encoded = (timestamp * mod) % mod_scalar
    if encoded == 0:
        print timestamp
    encoded_b36 = base10_to_base36(encoded)
    return encoded, encoded_b36


def decode(encoded, mod_scalar_inv=97982421746426015159,
           mod=100000000000000000000):
    return (encoded * mod_scalar_inv) % mod


def get_mapping_file(number_of_ids, id_prefix=None, header='#SampleID'):
    if id_prefix != None:
        id_prefix = id_prefix + ':'
    else:
        id_prefix = ''
    mapping_ids = [header]
    for i in range(number_of_ids):
        time.sleep(0.0001)
        time_stamp = int(time.time() * 100000)
        encoded_id = '%s%s' % (id_prefix, encode(time_stamp)[1])
        mapping_ids.append(encoded_id)
    return '\n'.join(mapping_ids)
