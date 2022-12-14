def nameUniqueEmails(emails):
    """This function returns filtered mails in set """
    seen = set()
    for email in emails:
        name, domain = email.split('@')
        local = name.split('+')[0].replace(".", "")
        seen.add(local + "@" + domain)
    return len(seen)


print(nameUniqueEmails(["testemail+alex@leetcode.com", "test.e.mail+bob.cathy@leetcode.com",
                        "testemail+david@lee.tcode.com"]))
