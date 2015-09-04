from difflib import get_close_matches, unified_diff


def fix_ids(correct_fh, diff_fh, match=.5):
    correct_ids = get_ids(correct_fh)
    fixed_ids = []
    for line in diff_fh:
        line = line.strip().split('\t')
        if line[0].startswith('#'):
            fixed_ids.append('\t'.join(line))
        elif line[0] in correct_ids:
            fixed_ids.append('\t'.join(line))
        else:
            fixed_id = get_close_matches(line[0], correct_ids, 1, match)
            line[0] = fixed_id[0]
            line = '\t'.join(line)
            fixed_ids.append(line)

    return '\n'.join(fixed_ids)


def get_diffs(lines1, lines2):
    diff_description = []
    for line in unified_diff(lines1, lines2):
        diff_description.append(line)
    return diff_description
