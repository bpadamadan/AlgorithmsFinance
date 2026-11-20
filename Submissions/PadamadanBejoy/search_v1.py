def linear_search(ids, queries):
    results = []

    for query in queries:
        found = False

        for value in ids:
            if value == query:
                found = True
                break

        results.append(found)

    return results