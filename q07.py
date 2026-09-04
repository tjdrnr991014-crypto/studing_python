email = "hong.gildong@example.com"
id = email[:12]
domain = email[13:]
domain_first = domain.split('.')

print(email.find('@'))
print(id, domain)
print(email.split('@'))
print(id.upper())
print(domain[:7])