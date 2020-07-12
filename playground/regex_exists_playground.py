import argparse
import asyncio
import logging
import random

from py_asyncio_regex.regex_exists import async_regex_exists

LOGGER = logging.getLogger(__name__)


async def regex_exists_with_sleep(task_id, regex_pattern, string_value):
    random_int = random.randint(1, 10)
    await asyncio.sleep(random_int)
    return await async_regex_exists(regex_pattern, string_value), task_id, random_int


def _parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--regex-pattern', required=True)
    parser.add_argument('--string-values', nargs='+', required=True)
    return parser.parse_args()


async def _main():
    args = _parse_args()

    regex_pattern = args.regex_pattern
    string_values = args.string_values

    # Create async tasks
    task_list = []
    task_id = 0
    for string_value in string_values:
        task_id += 1
        task = asyncio.create_task(
            regex_exists_with_sleep(task_id, regex_pattern, string_value)
        )
        task_list.append(task)
    # Check how many tasks remaining
    active_task_count = len(asyncio.all_tasks()) - 1
    while active_task_count > 0:
        LOGGER.info("Active Tasks: %s", active_task_count)
        await asyncio.sleep(1)
        active_task_count = len(asyncio.all_tasks()) - 1
    # When all tasks complete, print the results
    for t in task_list:
        r, task_id, random_int = await t
        LOGGER.info("Task Id: %s, Result: %s, Random Sleep: %s",
                    task_id, r, random_int)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(_main())
