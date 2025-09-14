# Versions manager
# https://www.codewars.com/kata/5bc7bb444be9774f100000c3

class VersionManager:
    def __init__(self, version: str = ''):
        if not version.strip():
            version = '0.0.1'
        parts = version.split('.')
        nums = []
        try:
            for p in parts[:3]:
                nums.append(int(p))
        except ValueError:
            raise ValueError("Error occured while parsing version!")
        while len(nums) < 3:
            nums.append(0)
        self.version = nums
        self.versions = [self.version.copy()]

    def _save(self):
        self.versions.append(self.version.copy())

    def major(self):
        self.version[0] += 1
        self.version[1] = 0
        self.version[2] = 0
        self._save()
        return self

    def minor(self):
        self.version[1] += 1
        self.version[2] = 0
        self._save()
        return self

    def patch(self):
        self.version[2] += 1
        self._save()
        return self

    def rollback(self):
        if len(self.versions) < 2:
            raise IndexError("Cannot rollback!")
        self.versions.pop()
        self.version = self.versions[-1].copy()
        return self

    def release(self):
        return f"{self.version[0]}.{self.version[1]}.{self.version[2]}"





