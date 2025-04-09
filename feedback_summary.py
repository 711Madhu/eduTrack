from feedback_entry import collect_feedback
from score_calculator import calculate_average

def summarize_feedback(feedback_list, score_list):
    total = len(feedback_list)
    avg_score = calculate_average(score_list)
    summary = {
        "total_feedbacks": total,
        "average_score": avg_score,
        "top_feedback": feedback_list[0] if feedback_list else "N/A"
    }
    return summary
