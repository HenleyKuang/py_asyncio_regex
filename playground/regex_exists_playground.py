import argparse
import asyncio
import logging

from py_asyncio_regex.regex_exists import regex_exists

LOGGER = logging.getLogger(__name__)


def _parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--regex-pattern', required=True)
    parser.add_argument('--string-values', nargs='+', required=True)
    return parser.parse_args()


async def _main():
    args = _parse_args()

    regex_pattern = args.regex_pattern
    string_values = args.string_values

    task_list = []
    for string_value in string_values:
        task = asyncio.create_task(
            regex_exists(regex_pattern, string_value)
        )
        task_list.append(task)
    for t in task_list:
        r = await t
        LOGGER.info(r)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(_main())
