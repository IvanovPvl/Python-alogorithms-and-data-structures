import random

phrase = 'methinks it is like a weasel'

def generate_phrase():
    s = ''
    while len(s) < len(phrase):
        s += gen_random_char()

    return s

def generate_phrase_1(old):
    if old is '':
        return generate_phrase()

    s = ''
    for i, ch in enumerate(phrase):
        if ch != old[i]:
            s += gen_random_char()
        else:
            s += phrase[i]

    return s

def gen_random_char():
    num = random.randint(97, 123)
    if num == 123:
        num = 32

    return chr(num)

def check_phrase(s):
    mark = 0
    for i, ch in enumerate(s):
        if ch == phrase[i]:
            mark = mark + 1

    return mark

def run():
    random.seed()
    max_mark = 0
    count = 0
    all_count = 0
    max_mark_phrase = ''
    gen_phrase = ''

    while max_mark < len(phrase):
        # gen_phrase = generate_phrase()
        gen_phrase = generate_phrase_1(gen_phrase)
        mark = check_phrase(gen_phrase)
        if mark > max_mark:
            max_mark = mark
            max_mark_phrase = gen_phrase
            print(gen_phrase)

        if count == 1000:
            count = 0
            print("%s - max_mark:%d - all_count:%d" % (max_mark_phrase, max_mark, all_count))

        count = count + 1
        all_count = all_count + 1

    print("All count - %d" % (all_count))

run()
