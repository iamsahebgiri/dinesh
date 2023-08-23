import secrets


class Password:
    def help():
        return (
            "generate cryptographically secure password 'dig pwd.8 @127.0.0.1'"
        )

    def query(self, args):
        q = "".join(args)

        # if no args is provided make it length 10
        if q == "":
            q = "10"

        if q.isdigit():
            q = int(q)

            return secrets.token_urlsafe(q)[:q]
        else:
            raise Exception("malformed input, expects number only")
