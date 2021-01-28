# Stefan Bordei 2021
# Implementation of some of the objects in Pandas.


import numbers


class MySeries:
    def __init__(self, data, index=None, name=None):
        """
        Indexed series stored as a dict.

        :param data: list, dict
                    Contains data stored in series.
        :param index: array-like, optional
        """

        assert data is not None, "please provide data"
        assert isinstance(data, list) or isinstance(data, dict), \
            "data must be list or dict"
        assert index is None or len(data) == len(index), \
            "index len must be equal to data len"

        self.s_dict = {}
        self.name = name

        if isinstance(data, dict):
            self.s_dict = data
        else:
            # if data is a list check if an index list has been
            # provided and map the entries or map against default
            # indices
            idx = index if index is not None else range(len(data))
            for i, k in zip(idx, data):
                self.s_dict[i] = k

    def min(self):
        assert all(isinstance(val, numbers.Number) for val in self.s_dict.values()), \
            "min must be performed on numeric values"
        return min(self.s_dict.values())

    def max(self):
        assert all(isinstance(val, numbers.Number) for val in self.s_dict.values()), \
            "max must be performed on numeric values"
        return max(self.s_dict.values())

    def mean(self):
        assert all(isinstance(val, numbers.Number) for val in self.s_dict.values()), \
            "mean must be performed on numeric values"
        return sum(self.s_dict.values()) / len(self.s_dict.values())

    def print(self):
        for k, v in self.s_dict.items():
            print(f"{k}\t", end='')
            if isinstance(v, list):
                for item in v:
                    print(f"{item}\t", end='')
            else:
                print(f"{v}\t", end='')
            print()

    def item_at_ind(self, i):
        return self.s_dict[i]

    def size(self):
        return len(self.s_dict.values())

    def sort_by_index(self, index_list):
        keys = list(self.s_dict.keys())
        val = list(self.s_dict.values())
        sorted_dict = {}

        sorted_val = [val[j] for j in index_list]
        for k, v in zip(keys, sorted_val):
            sorted_dict[k] = v
        self.s_dict = sorted_dict


class MyDataFrame:
    def __init__(self, data, index=None):
        """
            Dataframe two-dimensional tabular data.
        :param data: dict
                    Contains data stored in DataFrame
        :param index: array-like, optional
                    Contains row label list
        """
        assert isinstance(data, dict), "data must be a dict"
        assert index is None or all(len(index) == len(val) for val in data.values()), \
            "the number of rows (index) must match the number items in data values"

        # DataFrame columns with name/label (MySeries list)
        self.columns = []
        for k, v in data.items():
            self.columns.append(MySeries(v, name=k))

        assert all(self.columns[0].size() == val.size() for val in self.columns), \
            "data values must have same len"

        # DataFrame row labels
        self.index = index if index is not None else range(self.columns[0].size())

    def min(self):
        for series in self.columns:
            try:
                print(f"{series.name:<12}\t{series.min():>12.2f}")
            except AssertionError:
                # skip invalid column types
                continue

    def max(self):
        for series in self.columns:
            try:
                print(f"{series.name:<12}\t{series.max():>12.2f}")
            except AssertionError:
                # skip invalid column types
                continue

    def mean(self):
        for series in self.columns:
            try:
                print(f"{series.name:<12}\t{series.mean():>12.2f}")
            except AssertionError:
                # skip invalid column types
                continue

    def print(self):
        print('\t', end='')
        for series in self.columns:
            print("{:^17} ".format(series.name), end='')
        print()
        for i in range(len(self.index)):
            print(f"{self.index[i]:<13}", end='')
            for j in range(len(self.columns)):
                print(f"{self.columns[j].item_at_ind(i):<19}", end='')
            print()

    def sort_values(self, column_name):
        sorted_index_list = []

        # find column to sort by and build the
        # corresponding ordered list of indices
        for col in self.columns:
            if col.name == column_name:
                sorted_index_list = [i[0] for i in sorted(enumerate(col.s_dict.values()),
                                                          key=lambda x: x[1])]
        if not sorted_index_list:
            print(f"Column {column_name} not found. No sorting will be performed.")
            return

        # sort all column series and the df index by sorted_index_list
        for col in self.columns:
            col.sort_by_index(sorted_index_list)
        self.index = [self.index[x] for x in sorted_index_list]


# Template:

d = {'Sun Hours': [4.5,4.0,5.1,5],
     'Max Temp': [19.6,19.1,19.6,20.0],
     'Min Temp': [12.7,12.5,13.3,12.1],
     'Rain (mm)': [82,109,65,76],
     'Rain Days': [13,20,10,9.7]}
df1 = MyDataFrame(d)
df2 = MyDataFrame(d, index = ['Clare', 'Galway','Dublin', 
  'Wexford'])

df2.print()

df2.sort_values('Rain (mm)')
df2.print()
