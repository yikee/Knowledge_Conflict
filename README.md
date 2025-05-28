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

## Citing
If you found this work helpful, please consider starring this repository and citing our paper as shown below:

```latex
@article{wang2023resolving,
  title={Resolving knowledge conflicts in large language models},
  author={Wang, Yike and Feng, Shangbin and Wang, Heng and Shi, Weijia and Balachandran, Vidhisha and He, Tianxing and Tsvetkov, Yulia},
  journal={arXiv preprint arXiv:2310.00935},
  year={2023}
}
