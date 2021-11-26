import typing as t
from pathlib import Path
from transformers import (AutoModelForSeq2SeqLM, AutoTokenizer,
                          SummarizationPipeline)

main_path = Path(__file__).parent
SUMMARIZATION_MODEL_DIR = (main_path / '../checkpoint/').resolve()

summarization_pipeline = SummarizationPipeline(
    model=AutoModelForSeq2SeqLM.from_pretrained(SUMMARIZATION_MODEL_DIR),
    tokenizer=AutoTokenizer.from_pretrained(
        SUMMARIZATION_MODEL_DIR,
        skip_special_tokens=True,
    ),
    device=-1,
)

class Ml:
    @staticmethod
    def predict_single(text: str) -> str:
        summary = summarization_pipeline([text])
        return summary
    @staticmethod
    def predict_multiple(text_list: t.List[str]) -> t.List[str]:
        summaries = []
        for text in text_list:
            summaries.append(summarization_pipeline([text]))
        return summaries