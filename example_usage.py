"""
Demonstration of Concolic Symbolic Execution Branch Inverter Skill
"""

from client import ConcolicExecutor

def target_function(x: int, y: int, tracker: ConcolicExecutor) -> str:
    if tracker.record_branch("b1_x_gt_0", x > 0):
        if tracker.record_branch("b2_y_gt_10", y > 10):
            return "PATH_A"
        else:
            return "PATH_B"
    else:
        return "PATH_C"

def main():
    print("=== Concolic Execution & Symbolic Branch Inversion Demonstration ===")
    tracker = ConcolicExecutor()

    # Concrete run 1: x = 5, y = 3
    result = target_function(5, 3, tracker)
    print(f"Run 1: Result = {result}")
    print(f"Recorded Path Decisions: {tracker.branch_history}")

    assert result == "PATH_B"
    assert tracker.branch_history == [("b1_x_gt_0", True), ("b2_y_gt_10", False)]

    # Generate inverted target paths for subsequent exploration
    inverted_targets = tracker.get_inverted_targets()
    print(f"\nGenerated Inverted Branch Targets ({len(inverted_targets)} targets):")
    for t in inverted_targets:
        print(f"  Target: Invert {t['target_branch']} -> {t['inverted_condition'][1]} (Prefix: {t['required_prefix']})")

    assert len(inverted_targets) == 2
    # Inverting b2 yields PATH_A (y > 10)
    assert inverted_targets[1]["target_branch"] == "b2_y_gt_10"
    assert inverted_targets[1]["inverted_condition"] == ("b2_y_gt_10", True)

    print("\nConcolic Execution Branch Inverter Verification PASS!")

if __name__ == "__main__":
    main()
