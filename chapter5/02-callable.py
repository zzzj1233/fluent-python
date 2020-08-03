class Testc:
    def __call__(self, *args, **kwargs):
        return "ok"


# True
print(callable(Testc))

# True
print(callable(Testc()))
