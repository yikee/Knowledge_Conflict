## Resolving Knowledge Conflicts in Large Language Models <a href="https://arxiv.org/pdf/2310.00935">

<div align="center">
  <b>Yike Wang*, Shangbin Feng*, Heng Wang, Weijia Shi, Vidhisha Balachandran, Tianxing He, Yulia Tsvetkov</b>
  <br><br>
  <a href="https://arxiv.org/pdf/2310.00935"><img src="https://img.shields.io/badge/Paper-arXiv-orange"></a>
</div>

## Dataset
The top-level keys in the json file correspond to primary fields, and each data point within a field is represented as a dictionary, with the following key-value pairs:
- `main_entity`(str): an entity from the generated entity list
- `parametric_knowledge`(str): extracted parametric knowledge about the `main_entity`
- `named_entity_lst`(lst): named entities with corresponding types returned by NER models
- `conflict_generation_method`(str): either "substitution" or "shuffling", representing in-domain named entity substitution and in-domain entity shuffling respectively
- `entity_before`(str): an entity originally presents in the `parametric_knowledge` before substitution or shuffling
- `entity_after`(str): the entity that replaces the `entity_before` in cases of substitution or shuffling
- `conflicting_knowledge`(str): the conflicting knowledge created by substitution or shuffling
- `question_about_conflicting_segments`(str): a question related to the conflicting segments of `conflicting_knowledge`
- `question_about_nonconflicting_segments`(str): a question related to the nonconflicting segments of `conflicting_knowledge`

## Setup
Install dependencies:
```bash
pip install -r requirements.txt
```

Set your OpenAI API key:
```bash
export OPENAI_API_KEY="your_openai_api_key"
```

## Experiments
The exact prompts used for all experiments are included in the `prompts` folder, with the corresponding samples provided in Appendix E of the paper.
You can run the experiments using the following command:
```bash
# example
python run.py \
  --input_file dataset/gpt-3.5-turbo/data.json \
  --prompt_file prompts/task2/zero-shot.prompt \
  --output_file results/task2/zero-shot.json
```

## Questions
If you have any questions or comments about our paper or data, feel free to reach out via email at `yikewang@cs.washington.edu`. We will do our best to respond within one business day.

## Citing
If you found this work helpful, please consider starring this repository and citing our paper as shown below:

```latex
@article{wang2023resolving,
  title={Resolving knowledge conflicts in large language models},
  author={Wang, Yike and Feng, Shangbin and Wang, Heng and Shi, Weijia and Balachandran, Vidhisha and He, Tianxing and Tsvetkov, Yulia},
  journal={arXiv preprint arXiv:2310.00935},
  year={2023}
}
