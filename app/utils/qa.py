def answer_question(qa_pipeline, question, context):
    """
    Answer a question given a context using a QA pipeline.
    Args:
        qa_pipeline: Hugging Face QA pipeline.
        question (str): The question to answer.
        context (str): The context from which to extract the answer.
    Returns:
        dict: Answer with score and start/end positions.
    """
    result = qa_pipeline(question=question, context=context)
    return {
        "answer": result["answer"],
        "score": result["score"],
        "start": result["start"],
        "end": result["end"]
    }