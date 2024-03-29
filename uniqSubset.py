# Write a Python class to get all possible unique subsets from a set of distinct integers.


class Sub:
    def subset(self,curr,series):
        if series:
            return self.subset(curr,series[1:]) + self.subset(curr+ [series[0]],series[1:])
        return [curr]
s = Sub()
print(s.subset([],[2,3,4]))