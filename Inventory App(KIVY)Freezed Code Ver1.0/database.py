import datetime


class DataBase:
    def __init__(self, filelocation):
        self.filelocation = filelocation
        self.data = None
        self.load_data = None
        self.file = None
        self.string = None
        self.counter = None
        self.load()


    def load(self):
        self.file = open(self.filelocation, "r")
        self.load_data = []

        for line in self.file:
            # print(line)

            name1, name, types, location, created = line.strip().split(";")
            # print((str(name).lower(), str(types).lower(), location, created))
            # self.data[name.lower()] = (str(name).lower(), str(types).lower(), location, created)
            self.load_data.append((str(name).lower(), str(types).lower(), location, created))

            # print(self.load_data)

        self.file.close()

    def get_data(self, name):
        self.load()
        search = name.lower()
        # print(search)
        return [self.load_data[i] for i, j in enumerate(self.load_data) if str(j[0]).lower().startswith(search[:2]) or str(j[1]).lower().startswith(search[:2])]

        # return list(self.data[name1] for name1, types in self.data.items() if str(name1).lower().startswith(search[:2]) or str(types[1]).lower().startswith(search[:2]))

    def add_data(self, name, types, location):
        self.data ={}
        if name.strip() not in self.data:
            self.data[name.strip()] = (name.strip(), types.strip(), location.strip(), DataBase.get_date())
            self.save()
            return 1
        else:
            print("name exists already")
            return -1

    # def validate(self, name):
    #     if self.get_user(name) != -1:
    #         return self.data[name][0] == types
    #     else:
    #         return False

    def save(self):
        with open(self.filelocation, "a") as f:
            for user in self.data:
                f.write(user.lower() + ";" + self.data[user][0].lower() + ";" + self.data[user][1].lower() + ";" + self.data[user][2] +  ";" + self.data[user][3] +"\n")

    def delete_everything(self):
        open(self.filelocation, 'w').close()

    def delete_Product(self, sel_del_data):
        self.load()
        # search = name.lower()
        # print(search)
        # return [self.load_data[i] for i, j in enumerate(self.load_data)]
        print("Deleted")

        with open(self.filelocation, "r") as f:

            lines = f.readlines()

        with open(self.filelocation, "w") as f:

            for line in lines:

                if line.strip("\n") != sel_del_data:
                    f.write(line)

    @staticmethod
    def get_date():
        return str(datetime.datetime.now()).split(" ")[0]