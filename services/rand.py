import random


class Random:
    def help():
        return "generate random numbers 'dig rand.1-100 @127.0.0.1'"

    def query(self, args):
        q = "".join(args)
        min_val, max_val = q.split("-")
        if min_val.isdigit() and max_val.isdigit():
            min_val = int(min_val)
            max_val = int(max_val)

            if min_val > max_val:
                min_val, max_val = max_val, min_val

            return random.randint(min_val, max_val)
        else:
            raise Exception("malformed input, expects number only")
