def delete_nth(order, max_e):
    count = {}
    res = []
    for i in order:
        if i in count and count[i] < max_e:
            res.append(i)
            count[i] += 1
        elif i not in count:
            res.append(i)
            count[i] = 1
    return res

