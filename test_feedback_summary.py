from feedback_summary import summarize_feedback

def test_summarize_feedback():
    feedbacks = ["Great", "Average", "Needs improvement"]
    scores = [80, 70, 90]
    summary = summarize_feedback(feedbacks, scores)
    assert summary["total_feedbacks"] == 3
    assert summary["average_score"] == 80
