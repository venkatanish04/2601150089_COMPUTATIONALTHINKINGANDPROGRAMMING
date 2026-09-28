import asyncio
import aiohttp
import requests
import time


# =========================================================
# URLS TO CRAWL
# =========================================================

URLS = [
    "https://example.com",
    "https://httpbin.org/get",
    "https://www.python.org",
    "https://www.google.com",
    "https://httpbin.org/status/200",
]


# =========================================================
# SEQUENTIAL CRAWLER
# =========================================================

def sequential_crawler(urls: list[str]) -> list[tuple[str, int]]:
    results: list[tuple[str, int]] = []

    for url in urls:
        try:
            response = requests.get(url, timeout=10)
            results.append((url, response.status_code))
            print(f"Sequential: {url} -> {response.status_code}")

        except requests.RequestException as error:
            print(f"Sequential Error: {url} -> {error}")
            results.append((url, 0))

    return results


# =========================================================
# ASYNCHRONOUS CRAWLER WITH RETRIES
# =========================================================

async def fetch_with_retry(
    session: aiohttp.ClientSession,
    url: str,
    semaphore: asyncio.Semaphore,
    retries: int = 3
) -> tuple[str, int]:

    for attempt in range(1, retries + 1):

        try:
            async with semaphore:

                async with session.get(
                    url,
                    timeout=aiohttp.ClientTimeout(total=10)
                ) as response:

                    await response.read()

                    print(
                        f"Async: {url} -> "
                        f"{response.status}"
                    )

                    return url, response.status

        except (
            aiohttp.ClientError,
            asyncio.TimeoutError
        ) as error:

            print(
                f"Retry {attempt}/{retries}: "
                f"{url} -> {error}"
            )

            if attempt < retries:
                await asyncio.sleep(attempt)

    return url, 0


async def asynchronous_crawler(
    urls: list[str],
    concurrency: int = 3
) -> list[tuple[str, int]]:

    semaphore = asyncio.Semaphore(concurrency)

    async with aiohttp.ClientSession() as session:

        tasks = [
            asyncio.create_task(
                fetch_with_retry(
                    session,
                    url,
                    semaphore
                )
            )
            for url in urls
        ]

        results = await asyncio.gather(*tasks)

    return results


# =========================================================
# MAIN PROGRAM
# =========================================================

def main() -> None:

    print("=" * 60)
    print("SEQUENTIAL WEB CRAWLER")
    print("=" * 60)

    start_time = time.perf_counter()

    sequential_results = sequential_crawler(URLS)

    sequential_time = time.perf_counter() - start_time


    print("\n" + "=" * 60)
    print("ASYNCHRONOUS WEB CRAWLER")
    print("=" * 60)

    start_time = time.perf_counter()

    async_results = asyncio.run(
        asynchronous_crawler(
            URLS,
            concurrency=3
        )
    )

    async_time = time.perf_counter() - start_time


    # =====================================================
    # PERFORMANCE COMPARISON
    # =====================================================

    print("\n" + "=" * 60)
    print("PERFORMANCE COMPARISON")
    print("=" * 60)

    print(
        f"Sequential Time   : "
        f"{sequential_time:.4f} seconds"
    )

    print(
        f"Asynchronous Time : "
        f"{async_time:.4f} seconds"
    )

    if async_time > 0:
        speedup = sequential_time / async_time

        print(
            f"Speedup            : "
            f"{speedup:.2f}x"
        )

    print("\nSequential Results:")
    for url, status in sequential_results:
        print(f"{url} -> {status}")

    print("\nAsynchronous Results:")
    for url, status in async_results:
        print(f"{url} -> {status}")


# =========================================================
# PROGRAM ENTRY POINT
# =========================================================

if __name__ == "__main__":
    main()