s = '"Hd" "Td"'
# Remove unwanted characters and split
cleaned = s.strip().replace('"', '').split()
print(cleaned)  # Output: ['H', 'T']
