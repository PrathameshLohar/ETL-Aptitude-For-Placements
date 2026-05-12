import os
import json
import re

def parse_aptitude_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception:
        return None

    # Regex to handle varied text spacing around boundaries
    problem_match = re.search(r'Problem:\s*(.*?)\s*Solution:', content, re.DOTALL | re.IGNORECASE)
    solution_match = re.search(r'Solution:\s*(.*)', content, re.DOTALL | re.IGNORECASE)

    if not problem_match or not solution_match:
        return None

    problem = problem_match.group(1).strip()
    solution = solution_match.group(1).strip()

    return {
        "messages": [
            {
                "role": "system",
                "content": "You are an expert aptitude trainer. Solve the problem with a clear, step-by-step explanation and provide the final answer."
            },
            {
                "role": "user",
                "content": problem
            },
            {
                "role": "assistant",
                "content": solution
            }
        ]
    }

def process_nested_directories(root_dir, output_file):
    dataset = []
    
    # os.walk automatically visits every subfolder
    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            # Skip the root README file
            if filename.lower() == "readme.md":
                continue
                
            file_path = os.path.join(dirpath, filename)
            data_point = parse_aptitude_file(file_path)
            
            if data_point:
                dataset.append(data_point)

    # Write all data points out as a standard Hugging Face JSONL dataset
    with open(output_file, 'w', encoding='utf-8') as out_f:
        for item in dataset:
            out_f.write(json.dumps(item, ensure_ascii=False) + '\n')
            
    print(f"Extraction Complete! Processed {len(dataset)} aptitude problems into '{output_file}'.")

if __name__ == "__main__":
    # '.' targets the folder where you run the script
    process_nested_directories('.', 'smollm2_aptitude_dataset.jsonl')
