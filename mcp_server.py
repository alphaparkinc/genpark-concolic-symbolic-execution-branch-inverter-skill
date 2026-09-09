"""
MCP Server for Concolic Symbolic Execution Branch Inverter Skill
"""

import json
import sys
from client import ConcolicExecutor

def handle_call(name: str, args: dict) -> dict:
    if name == "invert_execution_path":
        tracker = ConcolicExecutor()
        for bid, val in args.get("branches", [["b1", True], ["b2", False]]):
            tracker.record_branch(bid, val)
        targets = tracker.get_inverted_targets()
        return {"inverted_targets": targets}
    return {"error": f"Unknown tool: {name}"}

def main():
    for line in sys.stdin:
        if not line.strip():
            continue
        req = json.loads(line)
        res = handle_call(req.get("method"), req.get("params", {}))
        sys.stdout.write(json.dumps(res) + "\n")
        sys.stdout.flush()

if __name__ == "__main__":
    main()
