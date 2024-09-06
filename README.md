# Knowledge Conflict

This repository contains the data for [Resolving Knowledge Conflicts in Large Language Models](https://arxiv.org/abs/2310.00935v2) using the KNOWLEDGE CONFLICT framework.

----------------------------------------------------
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

## Citing
If you use our code or data, please cite our paper:

```latex
@article{wang2023resolving,
  title={Resolving knowledge conflicts in large language models},
  author={Wang, Yike and Feng, Shangbin and Wang, Heng and Shi, Weijia and Balachandran, Vidhisha and He, Tianxing and Tsvetkov, Yulia},
  journal={arXiv preprint arXiv:2310.00935},
  year={2023}
}
