import asyncio
import re


async def async_regex_exists(pattern, string):
    return bool(re.search(pattern, string))
