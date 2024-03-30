s_cnt = int(input())
s_list = [input() for _ in range(s_cnt)]
m_cnt = int(input())
m_list = [input() for _ in range(m_cnt)]


def fill_in_blank(words, reserves):
    if len(words) == 1:
        return reserves[0]

    hints = []
    q_idx = 0

    for i in range(len(words)):
        if words[i] == "?":
            if i > 0:
                hints.append(words[i - 1][-1])
                q_idx = 1
            if i < len(words) - 1:
                hints.append(words[i + 1][0])

        if words[i] in reserves:
            reserves.remove(words[i])

    for reserve in reserves:
        if len(hints) == 2 and reserve[0] == hints[0] and reserve[-1] == hints[1]:
            return reserve

        elif len(hints) == 1:
            if reserve[0] == hints[0] and q_idx > 0:
                return reserve

            elif reserve[-1] == hints[0] and q_idx == 0:
                return reserve


print(fill_in_blank(s_list, m_list))