import os

path = os.path.join(os.path.dirname(__file__), "unstructured")
print(path)

# for i, file in enumerate(os.listdir(path)):
#       print("renaming: " + file + "...")
#       os.rename(
#             os.path.join(path, file), 
#             os.path.join(path, ''.join([str(i), '.jpg']))
#       )
  