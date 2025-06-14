import argparse
import json
import os
from openai import OpenAI
client = OpenAI()

from time import sleep
from tqdm import tqdm
from tenacity import retry, stop_after_attempt, wait_random_exponential

# @retry(wait=wait_random_exponential(min=1, max=30), stop=stop_after_attempt(10))
def get_resp(prompt, temperature, maxtokens):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{'role': 'user', 'content': prompt}],
        temperature=temperature,
        max_tokens=maxtokens
    )
    return response.choices[0].message.content

# Modify this based on your specific task
def get_prompt(template, context, question):
    return template.format(context=context, question=question)

def main(args):
    if not os.getenv("OPENAI_API_KEY"):
        raise EnvironmentError("OPENAI_API_KEY environment variable not set")

    with open(args.input_file, "r") as f:
        data = json.load(f)

    with open(args.prompt_file, "r") as f:
        prompt_template = f.read().rstrip("\n")

    # Modify this based on your specific task
    context_lst = [dict["conflicting_knowledge"] for dict_lst in data.values() for dict in dict_lst]
    question_lst = [dict["question_about_conflicting_segments"] for dict_lst in data.values() for dict in dict_lst]

    results = []
    for context, question in tqdm(zip(context_lst, question_lst), total=len(context_lst), desc="Generating responses"):
        prompt = get_prompt(prompt_template, context, question)
        result = get_resp(
            prompt,
            args.temperature,
            args.maxtokens
        )
        results.append(result)
        sleep(0.05)

    os.makedirs(os.path.dirname(args.output_file), exist_ok=True)
    with open(args.output_file, "w") as f:
        json.dump(results, f, indent=2)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_file", type=str, required=True, help="Path to input JSON file")
    parser.add_argument("--prompt_file", type=str, required=True, help="Path to prompt template file")
    parser.add_argument("--output_file", type=str, required=True, help="Path to save output JSON file")
    parser.add_argument("--temperature", type=float, default=0.0, help="Sampling temperature")
    parser.add_argument("--maxtokens", type=int, default=128, help="Maximum number of output tokens")

    args = parser.parse_args()
    main(args)