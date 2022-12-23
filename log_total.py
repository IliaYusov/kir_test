errors = {}

with open("log.txt") as f:
    for line in f:
        time, uri, error = line.strip().split(';')
        errors[uri] = errors.setdefault(uri, {error: 0})
        errors[uri][error] = errors[uri].setdefault(error, 0)
        errors[uri][error] += 1

print(errors)
