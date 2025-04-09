from feedback_entry import collect_feedback

def test_collect_feedback():
    fb = collect_feedback("Madhu", "VCS", "Extrodinary class")
    assert fb["name"] == "Madhu"
    assert fb["course"] == "VCS"
    assert fb["feedback"] == "Nice class"
