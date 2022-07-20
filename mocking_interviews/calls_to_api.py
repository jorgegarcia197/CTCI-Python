PAGE_SIZE = 10
MAX_SIZE = 103


class API:
    def fetch_page(self, page_num):
        if page_num > (MAX_SIZE/PAGE_SIZE):
            return {"next": None, "results": []}
        else:
            return {"next": page_num+1 if page_num <= (MAX_SIZE/PAGE_SIZE)-1 else None, "results": list(range(min(page_num*PAGE_SIZE, (page_num+1)*PAGE_SIZE), min((page_num+1)*PAGE_SIZE, MAX_SIZE)))}



class Fetcher:
    def __init__(self):
        self.cache = []
        self.api = API()
        self.page_size = len(self.api.fetch_page(0)["results"])
        self.page = 0
        self.offset = 0

    def fetch_results(self, num_results):
        if num_results <= 0:
            self.cache = []
            self.offset = 0
            return []
        number_of_calls = num_results//self.page_size
        if self.cache:
            results = self.cache[:num_results]
            if num_results > len(self.cache):
                self.offset = (num_results + len(self.cache))//self.page_size
                number_of_calls += self.offset
                for num_page in range(self.offset, number_of_calls+1):
                    self.cache.extend(self.api.fetch_page(num_page)["results"])
        else:
            for num_page in range(self.offset, number_of_calls+1):
                self.cache.extend(self.api.fetch_page(num_page)["results"])

        results = self.cache[:num_results]
        self.cache = self.cache[num_results:]
        return results


def tests_cases():
    new_fetcher = Fetcher()
    test1 = new_fetcher.fetch_results(5)
    assert test1 == [0, 1, 2, 3, 4]
    test2 = new_fetcher.fetch_results(2)
    assert test2 == [5, 6]
    test3 = new_fetcher.fetch_results(8)
    assert test3 == [7, 8, 9, 10, 11, 12, 13, 14]
    test4 = new_fetcher.fetch_results(0)
    assert test4 == []
    test5 = new_fetcher.fetch_results(103)
    assert test5 == list(range(103))
    return "Tests passed"


if __name__ == "__main__":
    print(tests_cases())
