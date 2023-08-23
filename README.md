# Dinesh

An augmented DNS server providing useful utilities.

```
nc -vu 127.0.0.1 1053
dig +retry=0 -p 1053 @127.0.0.1 +noedns google.com
```

### Random Number

Generate random number between [min, max] both inclusive.
It is suitable for rolling dice [1-6], flipping coins [0-1], etc. Both the arguments, `min` and `max` are required.

#### Examples

```sh
dig rand.1-100 @127.0.0.1 +short
# "69"

dig rand.1-6 @127.0.0.1 +short
# "3"

dig rand.0-1 @127.0.0.1 +short
# "1"
```

### Password

Generate cryptographically secure password suitable for generating tokens and codes. In this case `length` is optional.

#### Examples

```sh
dig pwd @127.0.0.1 +short
# "7XcFMFO1KV"

dig pwd.32 @127.0.0.1 +short
# "Efe3301RDS7V3bdKHb_zcRBRG_EYnQH_"
```
