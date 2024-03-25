class Customer:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self._reviews = []

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        if not isinstance(value, str):
            raise ValueError("First name must be a string")
        if not 1 <= len(value) <= 25:
            raise ValueError("First name must be between 1 and 25 characters")
        self._first_name = value

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        if not isinstance(value, str):
            raise ValueError("Last name must be a string")
        if not 1 <= len(value) <= 25:
            raise ValueError("Last name must be between 1 and 25 characters")
        self._last_name = value

    def reviews(self):
        return self._reviews

    def restaurants(self):
        return list({review.restaurant for review in self._reviews})

    def num_negative_reviews(self):
        return sum(1 for review in self._reviews if review.rating < 3)

    def has_reviewed_restaurant(self, restaurant):
        return any(review.restaurant == restaurant for review in self._reviews)


class Restaurant:
    def __init__(self, name):
        self.name = name
        self._reviews = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("Name must be a string")
        if len(value) < 1:
            raise ValueError("Name must be 1 or more characters")
        self._name = value

    def reviews(self):
        return [review for review in Review.all if review.restaurant == self]

    def customers(self):
        return list({review.customer for review in Review.all if review.restaurant == self})

    def average_star_rating(self):
        ratings = [review.rating for review in self.reviews()]
        if ratings:
            return round(sum(ratings) / len(ratings), 1)
        return 0.0

    @classmethod
    def top_two_restaurants(cls):
        avg_ratings = {restaurant: restaurant.average_star_rating() for restaurant in cls.all if restaurant.reviews()}
        top_restaurants = sorted(avg_ratings, key=avg_ratings.get, reverse=True)[:2]
        return top_restaurants if top_restaurants else []

class Review:
    all = []  

    def __init__(self, customer, restaurant, rating):
        self.customer = customer
        self.restaurant = restaurant
        self.rating = rating
        customer.reviews().append(self)
        restaurant.reviews().append(self)  
        Review.all.append(self)
        
