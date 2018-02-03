import pandas


def get_heirarchy(csv_file):

    df = pandas.read_csv(csv_file)
    # print the column names)

    json_heirarchy = {}
    heirarchy_value = ""
    heirarchy_name = ""
    json_heirarchy_usage_part = {}
    usage_name = ""
    part_name = ""
    for column in df:
        heirarchy_value = ""
        heirarchy_name = ""
        for index, row in pandas.Series.iteritems(df[column]):
            # print (str(row))

            if len(heirarchy_value) == 0 and len(heirarchy_name) == 0:

                if "usageid" in column.lower():

                    if (len(str(row)) > 0 and str(row) != "nan"):
                        if ("Total" not in str(row)):
                            usage_name = str(row)
                            if index not in json_heirarchy_usage_part:
                                json_heirarchy_usage_part[index] = []
                        else:
                            if index not in json_heirarchy_usage_part:
                                json_heirarchy_usage_part[index] = []
                            json_heirarchy_usage_part[index].append(usage_name)
                            usage_name = ""

                    if (len(usage_name) > 0):
                        if index not in json_heirarchy_usage_part:
                            json_heirarchy_usage_part[index] = []
                        json_heirarchy_usage_part[index].append(usage_name)
                        usage_name = ""

                    continue

                if "partid" in column.lower():

                    if (len(str(row)) > 0 and str(row) != "nan"):
                        if ("Total" not in str(row)):
                            part_name = str(row)
                            if index not in json_heirarchy_usage_part:
                                json_heirarchy_usage_part[index] = []
                        else:
                            if index not in json_heirarchy_usage_part:
                                json_heirarchy_usage_part[index] = []
                            json_heirarchy_usage_part[index].append(part_name)
                            part_name = ""

                    if (len(part_name) > 0):
                        if index not in json_heirarchy_usage_part:
                            json_heirarchy_usage_part[index] = []
                        json_heirarchy_usage_part[index].append(part_name)

                    continue

            heirarchy_value = column
            if column not in json_heirarchy:
                json_heirarchy[heirarchy_value] = {}
            if len(str(row)) > 0 and len(heirarchy_value) > 0:
                if "Total" not in str(row) and str(row) != "nan":
                    heirarchy_name = str(row)
                    if heirarchy_name not in json_heirarchy[heirarchy_value]:
                        json_heirarchy[heirarchy_value][heirarchy_name] = []
                        json_heirarchy[heirarchy_value][heirarchy_name].append(index)

                elif ("Total" in str(row)):

                    json_heirarchy[heirarchy_value][heirarchy_name].append(index)
                    heirarchy_name = ""
                else:
                    if (len(heirarchy_name) > 0):
                        json_heirarchy[heirarchy_value][heirarchy_name].append(index)

    return json_heirarchy, json_heirarchy_usage_part
