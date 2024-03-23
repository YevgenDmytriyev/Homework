# 1 task

def has_hits(author_name):
    for user in users:
        if user["name"] == author_name:
            for item in user["items"]:
                if "reads" in item and item["reads"] > 1000:
                    return True
            break
    return False

users = [
    {
        "name": "Clark",
        "type": "Publisher",
        "items": [
            {
                "title": "The ABC of Blockchain",
                "status": "Draft",
                "reads": 10
            }
        ]
    },
    {
        "name": "Peter",
        "type": "Publisher",
        "items": []
    },
    {
        "name": "Samantha",
        "type": "Publisher",
        "items": [
            {
                "title": "The ABC of JavaScript",
                "status": "Published",
                "reads": 3254
            },
            {
                "title": "The XYZ of JavaScript",
                "status": "Published",
                "reads": 226
            }
        ]
    },
    {
        "name": "Mathilda",
        "type": "Reviewer",
        "items": [
            {
                "title": "The ABC of Blockchain",
                "status": "Pending"
            }
        ]
    }
]

print("Clark", has_hits("Clark"))
print("Peter", has_hits("Peter"))
print("Samantha", has_hits("Samantha"))
print("Mathilda", has_hits("Mathilda"))
print("Mario", has_hits("Mario"))


# 2 task

def author_average_reads(author_name):
    total_reads = 0
    article_count = 0
    for user in users:
        if user["name"] == author_name:
            if user["type"] == "Publisher" and user["items"]:
                for item in user["items"]:
                    if item.get("status") == "Published" and "reads" in item:
                        total_reads += item["reads"]
                        article_count += 1
            break
    if article_count > 0:
        return total_reads // article_count
    return 0

users = [
    {
        "name": "Clark",
        "type": "Publisher",
        "items": [
            {
                "title": "The ABC of Blockchain",
                "status": "Draft",
                "reads": 10
            }
        ]
    },
    {
        "name": "Peter",
        "type": "Publisher",
        "items": []
    },
    {
        "name": "Samantha",
        "type": "Publisher",
        "items": [
            {
                "title": "The ABC of JavaScript",
                "status": "Published",
                "reads": 3254
            },
            {
                "title": "The XYZ of JavaScript",
                "status": "Published",
                "reads": 226
            }
        ]
    },
    {
        "name": "Mathilda",
        "type": "Reviewer",
        "items": [
            {
                "title": "The ABC of Blockchain",
                "status": "Pending"
            }
        ]
    }
]

print("Clark", author_average_reads("Clark"))
print("Peter", author_average_reads("Peter"))
print("Samantha", author_average_reads("Samantha"))
print("Mathilda", author_average_reads("Mathilda"))
print("Mario", author_average_reads("Mario"))


# 3 task

def author_is_popular(author_name):
    user = next((user for user in users if user["name"] == author_name), None)
    if user and user["type"] == "Publisher" and any(item.get("status") == "Published" for item in user["items"]):
        total_reads = sum(item["reads"] for item in user["items"] if item.get("status") == "Published" and "reads" in item)
        average_reads = total_reads / len([item for item in user["items"] if item.get("status") == "Published" and "reads" in item])
        return average_reads > 1000
    return False

users = [
    {
        "name": "Clark",
        "type": "Publisher",
        "items": [
            {
                "title": "The ABC of Blockchain",
                "status": "Draft",
                "reads": 10
            }
        ]
    },
    {
        "name": "Peter",
        "type": "Publisher",
        "items": []
    },
    {
        "name": "Samantha",
        "type": "Publisher",
        "items": [
            {
                "title": "The ABC of JavaScript",
                "status": "Published",
                "reads": 3254
            },
            {
                "title": "The XYZ of JavaScript",
                "status": "Published",
                "reads": 226
            }
        ]
    },
    {
        "name": "Mathilda",
        "type": "Reviewer",
        "items": [
            {
                "title": "The ABC of Blockchain",
                "status": "Pending"
            }
        ]
    }
]

print("Clark", author_is_popular("Clark"))
print("Peter", author_is_popular("Peter"))
print("Samantha", author_is_popular("Samantha"))
print("Mathilda", author_is_popular("Mathilda"))
print("Mario", author_is_popular("Mario"))
