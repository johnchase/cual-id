from difflib import get_close_matches, unified_diff
import collections

def fix_ids(correct_input, input_to_check, show, all, thresh=.5):
    if all:
        show = 'DFNV'

    corr_ids = [e.strip() for e in correct_input]
    broke_ids = [e.strip() for e in input_to_check]

    fixed_ids = []
    for broke_id in broke_ids:
        fixed_id = get_close_matches(broke_id, corr_ids, 1, thresh)
        if not fixed_id:
            fixed_id = ''
        else:
            fixed_id = fixed_id[0]
        fixed_ids.append(fixed_id)

    err_codes = get_err_codes(broke_ids, fixed_ids)
    return format_ouput(broke_ids, fixed_ids, err_codes, show)

def format_ouput(broke_ids, fixed_ids, err_codes, show):
    lines = []
    show = list(show)
    for line in zip(broke_ids, fixed_ids, err_codes):
        if any(i in list(line[2]) for i in show):
            lines.append('\t'.join(line))
        else:
            pass
    return '\n'.join(lines)


def get_err_codes(broke_ids, fixed_ids, ):
    err_codes = []
    for broke_id, fixed_id in zip(broke_ids, fixed_ids):
        if fixed_id == '':
            err_code = 'N'
        elif broke_id == fixed_id:
            err_code = 'V'
        else:
            err_code = 'F'
        if fixed_ids.count(fixed_id) > 1 and fixed_id != '':
            err_code = 'D' + err_code
        err_codes.append(err_code)
    return err_codes



'''error codes
    * D: duplicate
+   * F: fixed
+*    N: not fixable
+*    V: valid (didn't need correction)'''
