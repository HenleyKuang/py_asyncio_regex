import asyncio
import re


async def regex_exists(pattern, string):
    return bool(re.search(pattern, string))
