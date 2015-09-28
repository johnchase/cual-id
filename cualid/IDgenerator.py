import time


def base10_to_base36(number, alphabet='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
    """Converts an integer to a base36 string."""
    if not isinstance(number, (int)):
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
        print(timestamp)
    encoded_b36 = base10_to_base36(encoded)
    return encoded, encoded_b36


def decode(encoded, mod_scalar_inv=97982421746426015159,
           mod=100000000000000000000):
    return (encoded * mod_scalar_inv) % mod


def get_cual_ids(number_of_ids, prefix=None):
    if prefix is None:
        prefix = ''
    time_prev = None
    c = 0
    while c < number_of_ids:
        time_stamp = int(time.time() * 100000)
        if time_stamp != time_prev:
            encoded_id = '%s%s' % (prefix, encode(time_stamp)[1])
            c += 1
            time_prev = time_stamp
            yield encoded_id
