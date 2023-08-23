import inflect

p = inflect.engine()


class Num2Word:
    def help():
        return "convert numbers to words 'dig words.1024 @127.0.0.1'"

    def query(self, args):
        q = "".join(args)

        if q.isdigit():
            q = int(q)
            return p.number_to_words(q)
        else:
            raise Exception("malformed input, expects number only")
