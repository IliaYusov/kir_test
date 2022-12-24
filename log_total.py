import argparse


def errors_count(file: str = 'log.txt', selected_errors: list = None) -> dict:
    """Counts errors in log file, sorted by URI.

    Keyword arguments:
    file -- file path (default: log.txt)
    selected_errors -- list of error names (default: all errors)

    Returns: dict of URIs which values are dicts of error names
    """
    errors = {}
    with open(file) as f:
        for line in f:
            time, uri, error = (i.strip() for i in line.split(';'))
            if selected_errors is None or error in selected_errors:
                errors[uri] = errors.setdefault(uri, {error: 0})
                errors[uri][error] = errors[uri].setdefault(error, 0)
                errors[uri][error] += 1
    return errors


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', default='log.txt')
    parser.add_argument('--errors', default=None, action='extend', nargs='*')
    args = parser.parse_args()
    print(errors_count(file=args.file, selected_errors=args.errors))
