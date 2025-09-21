from sortedcontainers import SortedList
class MovieRentingSystem:

    def __init__(self, n: int, entries: List[List[int]]):
        self.available = {}
        self.movieToShopPrice = {}
        self.rented = SortedList()

        for shop, movie, price in entries:
            if movie not in self.available:
                self.available[movie] = SortedList()
                self.movieToShopPrice[movie] = {}
            self.available[movie].add((price, shop))
            self.movieToShopPrice[movie][shop] = price
        

    def search(self, movie: int) -> List[int]:
        if movie not in self.available:
            return []
        return [shop for price, shop in self.available[movie][:5]]
        

    def rent(self, shop: int, movie: int) -> None:
        price = self.movieToShopPrice[movie][shop]
        self.available[movie].remove((price, shop))
        self.rented.add((price, shop, movie))
        

    def drop(self, shop: int, movie: int) -> None:
        price = self.movieToShopPrice[movie][shop]
        self.available[movie].add((price, shop))
        self.rented.remove((price, shop, movie))
        

    def report(self) -> List[List[int]]:
        return [[shop, movie] for price, shop, movie in self.rented[:5]]


# Your MovieRentingSystem object will be instantiated and called as such:
# obj = MovieRentingSystem(n, entries)
# param_1 = obj.search(movie)
# obj.rent(shop,movie)
# obj.drop(shop,movie)
# param_4 = obj.report()