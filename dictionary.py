# ---------------------- Task-1 ----------------------------
# Dictionary of students (id -> details)
student_data = {
    "id1": {"name": "Sara",  "class": "V", "subject_integration": "english, math, science"},
    "id2": {"name": "David", "class": "V", "subject_integration": "english, math, science"},
    # duplicate of id1
    "id3": {"name": "Sara",  "class": "V", "subject_integration": "english, math, science"},
    "id4": {"name": "Surya", "class": "V", "subject_integration": "english, math, science"},
}
result = {}
seen_keys = []  # using a list instead of set

for student_id, details in student_data.items():
    unique_key = (details["name"], details["class"],
                  details["subject_integration"])

    if unique_key not in seen_keys:
        seen_keys.append(unique_key)
        result[student_id] = details

# print output line by line
for k, v in result.items():
    print(k, ":", v)


# ---------------------- Task-2 ----------------------------
test_dict = {'Codingal': 2, 'is': 2, 'best': 2, 'for': 2, 'Coding': 1}

print("The original dictionary : " + str(test_dict))

K = 2
# Selective key values in dictionary
res = 0
for key in test_dict:
    if test_dict[key] == K:
        res = res + 1

print("Frequency of K is : " + str(res))
# ---------------------- Task-3 ----------------------------
country_code = {'Pakistan': '0092','Australia': '0025','Nepal': '00977'}

# search dictionary for country code of Pakistan
print("Country code for Pakistan -")
print(country_code.get('Pakistan', 'Not Found'))

# search dictionary for country code of Japan
print("Country code for Japan -")
print(country_code.get('Japan', 'Not Found'))
