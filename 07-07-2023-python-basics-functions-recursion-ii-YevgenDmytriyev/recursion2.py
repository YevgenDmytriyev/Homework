# task 1
def sum_series(n):
    if n <= 0:
        return 0
    else:
        return n + sum_series(n - 2)

print(sum_series(7))
print(sum_series(8))
print(sum_series(15))

# task 2
def drill_sum(data):
    total = 0
    for element in data:
        if isinstance(element, int):
            total += element
        elif isinstance(element, list):
            total += drill_sum(element)
    return total

test_data1 = [
    1,
    [1, 2],
    [1, [2, 3]],
    [1, [2, [3, 4]]],
    [1, [2, [3, [4, 5]]]],
]
test_data2 = [
    [1, [[2, 6], [3, 4]]],
    [[5, 6, [7, 8]], [2, [3, [4, 5]]]],
    [1, [2, 3]],
    [1, 2],
    1,
]
print(drill_sum(test_data1))
print(drill_sum(test_data2))

# task 3
def count_pages(pages):
    count = 0
    for page in pages:
        count += 1
        if "pages" in page:
            count += count_pages(page["pages"])
    return count

test_data1 = [
    {
        "title": "Home",
        "pages": [
            {
                "title": "About",
                "pages": [
                    {
                        "title": "The company"
                    },
                    {
                        "title": "Our services"
                    },
                    {
                        "title": "Our products"
                    },
                    {
                        "title": "Our deliveries",
                        "pages": [
                            {
                                "title": "National"
                            },
                            {
                                "title": "International"
                            }
                        ]
                    }
                ]
            },
            {
                "title": "Shop",
                "pages": [
                    {
                        "title": "Browse all"
                    },
                    {
                        "title": "Categories"
                    }
                ]
            },
            {
                "title": "My account",
                "pages": [
                    {
                        "title": "Settings"
                    },
                    {
                        "title": "Edit profile"
                    },
                    {
                        "title": "My transactions"
                    }
                ]
            }
        ]
    }
]

print(count_pages(test_data1))
