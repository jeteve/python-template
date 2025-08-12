"""One CLI."""

import sys


def one_main() -> int:
    """Run the main code."""
    print("Hello world from jeteve_template CLI!")  # noqa: T201
    return 0


# Development entry point
if __name__ == "__main__":
    sys.exit(one_main())
