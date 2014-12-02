__author__ = 'Goran Vejnovic'
import datetime

cache = {}


def decorator(function_to_decorate):
    def get_from_cache(param):
        if param in cache:
            result, date, count = cache[param]
            if count <= 10 and (date - datetime.datetime.today()).total_seconds() <= (5*60):
                print("From cache")
                cache[param] = (result, date, (count + 1))
                return result
            else:
                print("Calculation " + str(param))
                result = param*2
                date = datetime.datetime.today()
                cache[param] = (result, date, 1)
                return result
        else:
            print("Calculation " + str(param))
            result = param*2
            date = datetime.datetime.today()
            cache[param] = (result, date, 1)
            return result
        function_to_decorate(param)
    return get_from_cache


@decorator
def get_result(param):
    print(param)

for x in range(1,12):
   print("Poziv:"+str(x)+" "+str(get_result(2)))



