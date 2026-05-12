import os
import json
import re

def parse_file_with_metadata(file_path, topic_name):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception:
        return None

    # Extract text between boundaries
    problem_match = re.search(r'Problem:\s*(.*?)\s*Solution:', content, re.DOTALL | re.IGNORECASE)
    solution_match = re.search(r'Solution:\s*(.*)', content, re.DOTALL | re.IGNORECASE)

    if not problem_match or not solution_match:
        return None

    problem = problem_match.group(1).strip()
    solution = solution_match.group(1).strip()

    # Construct clean user prompt using folder name as metadata
    user_content = f"Topic: {topic_name}\nQuestion: {problem}"

    return {
        "messages": [
            {
                "role": "system",
                "content": "You are an expert aptitude trainer specializing in campus placement preparation. Solve the question with a clear, step-by-step explanation and provide the final answer."
            },
            {
                "role": "user",
                "content": user_content
            },
            {
                "role": "assistant",
                "content": solution
            }
        ]
    }

def process_all_topics(root_dir, output_file):
    dataset = []
    
    # List all items in the root folder
    for item in os.listdir(root_dir):
        item_path = os.path.join(root_dir, item)
        
        # Process only subdirectories (skipping root README.md and hidden folders)
        if os.path.isdir(item_path) and not item.startswith('.'):
            topic_name = item
            
            # Loop through all individual problem files inside the topic directory
            for filename in os.listdir(item_path):
                file_path = os.path.join(item_path, filename)
                
                if os.path.isfile(file_path):
                    data_point = parse_file_with_metadata(file_path, topic_name)
                    if data_point:
                        dataset.append(data_point)

    # Export to unified JSONL format
    with open(output_file, 'w', encoding='utf-8') as out_f:
        for data in dataset:
            out_f.write(json.dumps(data, ensure_ascii=False) + '\n')
            
    print(f"Dataset generated! Extracted {len(dataset)} items with metadata into '{output_file}'.")

if __name__ == "__main__":
    process_all_topics('.', 'metadata_aptitude_dataset.jsonl')
