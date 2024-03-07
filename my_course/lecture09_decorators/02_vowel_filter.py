def vowel_filter(function):
    def wrapper():
        vowels = ['a', 'e', 'o', 'u', 'y', 'i']
        result = function()
        return [x for x in result if x in vowels]
    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]
print(get_letters())