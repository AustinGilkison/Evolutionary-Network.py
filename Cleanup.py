import LogConfig


def empty_logs():
    """Empties the logs for the program to prepare it for commit."""

    with open(LogConfig.DEBUG_LOG, mode="w") as log:
        log.write("")


empty_logs()
