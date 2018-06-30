import json
import random


class FixtureGenerator:

    skip = 3
    
    def g_user_object(self, n):
        item = {
            "model": "users.user",
            "pk": n,
            "fields": {
                "username": "user{0:03d}".format(n),
                "nickname": "name{0:03d}".format(n),
            },
        }
        return item

    def g_profile_object(self, n, m):
        skip = self.skip
        l = list(filter(lambda x: not x == n, [i for i in range(skip, m + skip)]))
        follows = random.sample(l, m // 2)
        item = {
            "model": "djeeterprofile.djeeterprofile",
            "pk": n,
            "fields": {
                "user": n,
                "follows": follows
            },
        }
        return item

    def g_djeet_object(self, n, u, body):
        item = {
            "model": "djeet.djeet",
            "pk": n,
            "fields": {
                "user": u,
                "body": body,
                "created_at": "2018-06-26 00:00:0.000000+00"
            },
        }
        return item

    def g_fixture(self, m, d):
        skip = self.skip
        items = [self.g_user_object(i) for i in range(skip, m + skip)]
        items += [self.g_profile_object(i, m) for i in range(skip, m + skip)]
        for i in range(m):
            items += [self.g_djeet_object(i * d + j + skip, i + skip, "hoge") for j in range(d)]
        return json.dumps(items, indent=4)


def generate_fixture_file(path):
    generator = FixtureGenerator()
    with open(path, "w") as f:
        f.write(generator.g_fixture(100, 10))

if __name__ == "__main__":
    
    generate_fixture_file("djitter/fixtures/enliven.json")

