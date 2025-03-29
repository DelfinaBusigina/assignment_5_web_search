import pandas as pd
from terminal_coloring import prCyan, prLightPurple, prGreen

simple_json = {
  "name": "Alice",
  "age": 25,
  "city": "New York"
}

print(simple_json["age"])
# prCyan(type(simple_json))

simple_json_df = pd.DataFrame([simple_json])
prCyan(simple_json_df)

nested_dict = {
  "user": {
    "id": 101,
    "name": "Bob",
    "email": "bob@example.com",
    "preferences": {
      "theme": "dark",
      "notifications": True
    }
  }
}

print(nested_dict["user"]["preferences"]["theme"])

nested_dict_df = pd.DataFrame([nested_dict["user"]])
prLightPurple(nested_dict_df)
prLightPurple("=====================================================")

nested_dict_df_2 = pd.json_normalize(nested_dict["user"])
prLightPurple(nested_dict_df_2)

prLightPurple("=====================================================")

list_of_dict = {
  "employees": [
    {"id": 1, "name": "John", "role": "Developer"},
    {"id": 2, "name": "Sarah", "role": "Designer"},
    {"id": 3, "name": "Mike", "role": "Manager"}
  ]
}

print(list_of_dict["employees"][1]["role"])

list_of_dict_df = pd.DataFrame(list_of_dict["employees"])
prGreen(list_of_dict_df)

prGreen("=====================================================")
print()

mixed_type = {
  "company": "TechCorp",
  "departments": [
    {
      "name": "Engineering",
      "employees": ["Alice", "Bob", "Charlie"]
    },
    {
      "name": "Marketing",
      "employees": ["David", "Eve"]
    }
  ],
  "isHiring": True
}

print(mixed_type["departments"][1]["employees"])

mixed_type_df = pd.json_normalize(mixed_type["departments"])

mixed_type_df = mixed_type_df.explode("employees")

mixed_type_df = mixed_type_df.reset_index(drop=True) #after explode original ids are preserved, restart ids

prCyan(mixed_type_df[["employees", 'name']]) #reordering columns


prCyan("=====================================================")
print()


nested_json = {
  "store": {
    "books": [
      {"title": "Book A", "price": 10, "author": {"name": "Author 1", "country": "USA"}},
      {"title": "Book B", "price": 15, "author": {"name": "Author 2", "country": "UK"}}
    ],
    "location": {
      "city": "Los Angeles",
      "zip": "90001"
    }
  }
}

print(nested_json["store"]["books"][1]["author"]["country"])

nested_json_df = pd.json_normalize(nested_json["store"]["books"])
prLightPurple(nested_json_df)