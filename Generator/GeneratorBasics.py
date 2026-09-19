# generator i s one type of special function that returns values once at a time , instead of creating and storing all values in memory at once. It uses the yield statement to return values one at a time, allowing for efficient memory usage and lazy evaluation. Generators are useful for working with large datasets or streams of data where you don't want to load everything into memory at once.
# Yeild is ame like Returns ,  return returns a vlaue but yeild produce a value, aftrer return func end but after yeild func pause, Usually retun returns one result but yeild produce multiple results

#Next()-> ask for the next value from the generator, and it will continue executing the function until it reaches the next yield statement. If there are no more values to yield, it will raise a StopIteration exception.

def get_numbers():
    return ["one", "two", "three"]

def get_numbers_generator():
    yield "one"
    yield "two"
    yield "three"
            