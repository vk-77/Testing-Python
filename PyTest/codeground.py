import os

# 1. Get the directory of the current test file (PyTestDemo)
current_dir = os.path.dirname(__file__)

# 2. Go up one level to 'Testing-Python', then into 'data'
test_data_path = os.path.abspath(os.path.join(current_dir, "..", "Data", "test_e2eTestFramework.json"))
print('result of file is empty.')
print(current_dir)
print(test_data_path)
print(os.path.exists(test_data_path))