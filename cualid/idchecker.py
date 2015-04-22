from cualid.util import get_ids
from difflib import get_close_matches, unified_diff


def get_correct_ids(correct_fh, diff_fh, match=.5):
    correct_ids = get_ids(correct_fh)
    # diff_ids = get_ids(diff_fh)
    fixed_ids = []
    for line in diff_fh:
        line = line.strip().split('\t')
        if line[0].startswith('#'):
            pass
        elif line[0] in correct_ids:
            fixed_ids.append('\t'.join(line))
        else:
            fixed_id = get_close_matches(line[0], correct_ids, 1, match)
            try:
                line[0] = fixed_id[0]
            except:
                print line[0]
            line = '\t'.join(line)
            fixed_ids.append(line)

    # for i in diff_ids:
    #     fixed_id = get_close_matches(i, correct_ids, 1, match)
    #     if len(fixed_id) != 1:
    #         print 'need to do something here'
    #         fixed_ids.append(i[0])
    #     else:
    #         fixed_ids.append(fixed_id[0])
    # diff = get_diffs(diff_ids, correct_ids)
    # print type('\n'.join(fixed_ids))
    return '\n'.join(fixed_ids)
    # '\n'.join(diff)


def get_diffs(lines1, lines2):
    diff_description = []
    for line in unified_diff(lines1, lines2):
        diff_description.append(line)
    return diff_description
