from feedback_summary import summarize_feedback

def test_summarize_feedback():
    feedbacks = ["Great session", "Could be better"]
    scores = [8, 9]
    summary = summarize_feedback(feedbacks, scores)

    assert summary["total_feedbacks"] == 2
    assert summary["average_score"] == 8.5
    assert summary["top_feedback"] == "Great session"
