def linear_search_product(product_list, target_product):
  indices = []
  for i, product in enumerate(product_list):
      if product == target_product:
          indices.append(i)
  return indices

# Example usage:
products = ["apple","ice","banana", "apple", "ice","orange","ice","apple"]
target = "ice"
result = linear_search_product(products, target)
if result:
  print(f"The product '{target}' was found at indices: {result}")
else:
  print(f"The product '{target}' was not found in the list.")