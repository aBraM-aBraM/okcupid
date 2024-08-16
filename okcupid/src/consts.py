from pathlib import Path

PROJECT_DIR = Path(__file__).parent.parent.parent
SRC_DIR = PROJECT_DIR / "src"
TEST_DIR = PROJECT_DIR / "tests"
RESOURCES_DIR = TEST_DIR / "resources"

STACK_ORDER = [
    "SUPERLIKES",
    "JUST_FOR_YOU",
    "MATCH_PERCENTAGE",
    "STANDOUTS",
    "OUT_FOR_THE_DAY",
    "PENPAL",
]
