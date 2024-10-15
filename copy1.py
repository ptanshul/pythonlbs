import copy

original_dict = {
    "user1": ["book1", "book2"],
    "user2": ["book3", "book4"]
}

shallow_copy = copy.copy(original_dict)
deep_copy = copy.deepcopy(original_dict)

# Modify a nested list in the shallow copy
shallow_copy["user1"].append("book5")

print("Original:", original_dict)
# Output: Original: {'user1': ['book1', 'book2', 'book5'], 'user2': ['book3', 'book4']}
print("Shallow:", shallow_copy)
# Output: Shallow: {'user1': ['book1', 'book2', 'book5'], 'user2': ['book3', 'book4']}
print("Deep:", deep_copy)
# Output: Deep: {'user1': ['book1', 'book2'], 'user2': ['book3', 'book4']} 