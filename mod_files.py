def clear_csv_file(filename):
    f = open(filename, "w")
    f.close()


def write_column_titles(filename):
    with open(filename, "w") as f:
        f.write("{}".format("IP_address,Port,Country_City,Speed,Type,Anonymity,Last_Check"))


