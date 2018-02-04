import pandas


def get_hierarchy(csv_file):

    df = pandas.read_csv(csv_file)
    # print the column names)

    json_hierarchy = {}
    hierarchy_value = ""
    hierarchy_name = ""
    json_hierarchy_usage_part = {}
    usage_name = ""
    part_name = ""
    for column in df:
        hierarchy_value = ""
        hierarchy_name = ""
        for index, row in pandas.Series.iteritems(df[column]):

            if len(hierarchy_value) == 0 and len(hierarchy_name) == 0:

                if "usageid" in column.lower():

                    if (len(str(row)) > 0 and str(row) != "nan"):
                        if ("Total" not in str(row)):
                            usage_name = str(row)
                            if index not in json_hierarchy_usage_part:
                                json_hierarchy_usage_part[index] = []
                        else:
                            if index not in json_hierarchy_usage_part:
                                json_hierarchy_usage_part[index] = []
                            json_hierarchy_usage_part[index].append(usage_name)
                            usage_name = ""

                    if (len(usage_name) > 0):
                        if index not in json_hierarchy_usage_part:
                            json_hierarchy_usage_part[index] = []
                        json_hierarchy_usage_part[index].append(usage_name)
                        usage_name = ""

                    continue

                if "partid" in column.lower():

                    if (len(str(row)) > 0 and str(row) != "nan"):
                        if ("Total" not in str(row)):
                            part_name = str(row)
                            if index not in json_hierarchy_usage_part:
                                json_hierarchy_usage_part[index] = []
                        else:
                            if index not in json_hierarchy_usage_part:
                                json_hierarchy_usage_part[index] = []
                            json_hierarchy_usage_part[index].append(part_name)
                            part_name = ""

                    if (len(part_name) > 0):
                        if index not in json_hierarchy_usage_part:
                            json_hierarchy_usage_part[index] = []
                        json_hierarchy_usage_part[index].append(part_name)

                    continue

            hierarchy_value = column
            if column not in json_hierarchy:
                json_hierarchy[hierarchy_value] = {}
            if len(str(row)) > 0 and len(hierarchy_value) > 0:
                if "Total" not in str(row) and str(row) != "nan":
                    hierarchy_name = str(row)
                    if hierarchy_name not in json_hierarchy[hierarchy_value]:
                        json_hierarchy[hierarchy_value][hierarchy_name] = []
                        json_hierarchy[hierarchy_value][hierarchy_name].append(index)

                elif ("Total" in str(row)):

                    json_hierarchy[hierarchy_value][hierarchy_name].append(index)
                    hierarchy_name = ""
                else:
                    if (len(hierarchy_name) > 0):
                        json_hierarchy[hierarchy_value][hierarchy_name].append(index)

    return json_hierarchy, json_hierarchy_usage_part
