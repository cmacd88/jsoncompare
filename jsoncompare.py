## Load Dependencies
import json
from deepdiff import DeepDiff

## Load JSON files
def load_json(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)
    
## Compare the two JSON files
def compare_json_files(test_file, prod_file):
    test_data = load_json(test_file)
    prod_data = load_json(prod_file)
    
    differences = DeepDiff(test_data, prod_data, view='tree')
    return differences

## File paths
test_file = 'file01.json'  # Replace with the path to your test file
prod_file = 'file02.json'  # Replace with the path to your prod file

## Get differences
diff = compare_json_files(test_file, prod_file)

## Prettify differences
def prettify_differences(diff):
    if not diff:
        print("No differences found.")
        return
    
    print("\n--- Differences Found ---\n")
    
    # Extract and format changes
    for change_type, changes in diff.items():
        print(f"{change_type}:")
        for change in changes:
            if hasattr(change, 't1'):
                # For type changes, present the old and new values
                print(f"  - {change.path(output_format='list')}:\n"
                      f"      File1 Value: {change.t1}\n"
                      f"      File2 Value: {change.t2}")
            else:
                # For other change types (added, removed, etc.)
                print(f"  - {change}")
        print()

## Output differences
if diff:
    prettify_differences(diff)
else:
    print("No differences found.")
