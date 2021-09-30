import re
def fun(s):
    emailre = re.compile(r'''
    [a-zA-Z0-9-_]+
    @
    [a-zA-Z0-9]+
    \.[a-zA-Z]{1,3}
    ''',re.VERBOSE)

    match = emailre.findall(s)
    if s in match:
        return True
    else:
        return False

def filter_mail(emails):
    return filter(fun, emails)


n = int(raw_input())
emails = []
for i in range(n):
    emails.append(raw_input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)