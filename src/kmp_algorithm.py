def compute_pref_array(needle):
    if not needle:
        return [0]

    length_needle = len(needle)
    longest_pref_suf = [0] * length_needle
    prev_iter, curr_iter = 0, 1
    while curr_iter < length_needle:
        if needle[curr_iter] != needle[prev_iter]:
            if prev_iter != 0:
                prev_iter = longest_pref_suf[prev_iter - 1]
            else:
                longest_pref_suf[curr_iter] = 0
                curr_iter += 1
        else:
            longest_pref_suf[curr_iter] = prev_iter + 1
            prev_iter += 1
            curr_iter += 1

    return longest_pref_suf


def search_by_kmp(haystack, needle):
    if not needle:
        return []

    longest_pref_suf = compute_pref_array(needle)
    result_i = []
    needle_length = len(needle)
    haystack_length = len(haystack)
    i, j = 0, 0

    while i < haystack_length:
        if haystack[i] == needle[j]:
            i += 1
            j += 1
            if j == needle_length:
                result_i.append(i - needle_length)
                j = longest_pref_suf[j - 1]
        else:
            if j != 0:
                j = longest_pref_suf[j - 1]
            else:
                i += 1

    if len(result_i) == 0:
        return None
    return result_i
