class Env():
    def __init__(self, outer=None, binds=None, exprs=None):
        self.data = dict()
        self.outer = outer

        if binds:
            for i in range(len(binds)):
                if binds[i] == "&":
                    self.data[binds[i+1]] = exprs[i:]
                    break
                else:
                    self.data[binds[i]] = exprs[i]

    def set(self, key, value):
        self.data[key] = value
        return value

    def find(self, key):
        if key in self.data:
            return self
        elif self.outer:
            return self.outer.find(key)
        else:
            return None

    def get(self, key):
        env = self.find(key)
        # Note: `find` does not return the value directly, because value can be False or None which are falsy
        # So we will never really be able to tell if we found the value False/None or whether we actually defined
        # not find anything. This `find` is made to return whether the object exists in this environment or not
        if not env:
            raise Exception("'" + key + "' not found")
        return env.data[key]
