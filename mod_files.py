import pandas as pd


def clear_csv_file(filename):
    f = open(filename, "w")
    f.close()


def write_column_titles(filename):
    with open(filename, "w") as f:
        f.write("{}".format("IP_address,Port,Country_City,Speed,Type,Anonymity,Last_Check"))


def remove_empty_lines(input_csv_file, output_csv_file):
    df = pd.read_csv(input_csv_file)
    df.to_csv(output_csv_file, index=False)

