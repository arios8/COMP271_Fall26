def are_isomorphic(t:str, s:str) -> bool:
    max_length = 500

    #seeing if inouts are valid 
    result = (
        s is not None 
        and t is not None
        and s.isalpha()
        and t.isalpha()
        and len(s) == len(t)
        and len (s) > 0
        and len(t) <= max_length

    )

    if result:
        s_chars_already_seen = []
        t_chars_already_seen = []

    #loop needs to go until value is false or we exhaust length
    i = 0
    while i < len(s) and result:
        s_char = s[i]
        t_char = t[i]

        #for s string
        #if char from s been seen before, then order from position a 
        #must match current char from t
        s_char_seen = False
        a = 0
        while a < len(s_chars_seen):
            #current char from s has been seen then dont add to list of chars already seen
            if s_chars_already_seen[a] == s_char:
                #ath char from t must match current char from t
                s_chars_seen = True
                if t_chars_already_seen[a] != t_char:
                    result = False
            a += 1

        #for t string
        t_char_seen = False
        b = 0
        while b < len(t_chars_already_seen):
            if t_chars_already_seen[b] == t_char:
                #current char from t was seen needs to match order in which current char from s was also seen before
                #if not string are isomorphic
                t_chars_seen = True
                if s_chars_already_seen[b] != s_char:
                result = False
             b += 1

        #if neither cahr been seen, add them to "already seen" list
        #then continue with next position
        if not s_chars_seen and not t_chars_seen:
            s_chars_already_seen.append)s_char)
            t_chars_already_seen.append)t_char)

        i += 1

return result


def is_interleaved(s1, s2, s3):
    max_length = 100
    interleaving = 2

    #validating
    valid = (
        s1 is not None
        and s2 is not None
        and s3 is not None
        and len(s1) <= max_length
        and len(s2) <= max_length
        and len(s1) + len(s2) == len(s3)
        and s1.isalpha()
        and s2.isalpha()

    )

    is valid:
    #since valid, check for interleaving
    #i for tracking position s1, s2
    #x for tracking position s3
    i = 0
    x = 0

    s1_first = True
    s2_first = True

    #chars in s1 and s2
    while i < min(len(s1), len(s2)) and (s1_first or s2_first):
        s1_first = s1_first and (s1[1] == s3[x] and s2[i] == s3[x +1])
        s2_first = s2_first and (s2[i] == s3[x] and s1[i] == s3[x + 1])
        i =+ 1
        x += interleaving

    #checks remaining in s1 
    while i < len(s1) and (s1_first or s2_first):
        s1_first = s1_first and (s1[i] == s3[x])
        s2_first = s2_first and (s1[i] == s3[x])
        i =+ 1
        x += 1

    #check remaining in s2
    while i < len(s2) and (s1_first or s2_first):
        s1_first = s1_first and (s2[i] == s3[x])
        s2_first = s2_first and (s2[i] == s3[x])
        i += 1
        x =+ 1

    #final check 
    valid = s1_first or s2_first

return valid 


def contiguous_length(nums):
    #total num of elements in array
    n = len(nums)
    longest = 0

    #starting index of subarray
    i = 0
    while i < n:
        zeros = 0
        ones = 0

        #extend subarray to right 
        x = i
        while x < n:
            if nums[x] == 0:
                zeros =+ 1
            else:
                ones =+ 1

            if zeros == ones:
                length = x - i + 1
                if length > longest:
                    longest = length
            x =+ 1

        i += 1
    return longest




    

        
