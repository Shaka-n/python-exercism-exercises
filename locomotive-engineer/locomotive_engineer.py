"""Functions which helps the locomotive engineer to keep track of the train."""


def get_list_of_wagons(*args):
    """Return a list of wagons.

    :param: arbitrary number of wagons.
    :return: list - list of wagons.
    """
    return list(args)


def fix_list_of_wagons(each_wagons_id, missing_wagons):
    """Fix the list of wagons.

    :param each_wagons_id: list - the list of wagons.
    :param missing_wagons: list - the list of missing wagons.
    :return: list - list of wagons.
    """
    first, second, *rest = each_wagons_id
    each_wagons_id = rest + [first, second]
    loco, *rest = each_wagons_id
    return [loco] + missing_wagons + rest

def add_missing_stops(route, **kwargs):
    """Add missing stops to route dict.

    :param route: dict - the dict of routing information.
    :param: arbitrary number of stops.
    :return: dict - updated route dictionary.
    """

    route["stops"] = []
    for key, name in kwargs.items():
        route["stops"].append(name)
    return route



def extend_route_information(route, more_route_information):
    """Extend route information with more_route_information.

    :param route: dict - the route information.
    :param more_route_information: dict -  extra route information.
    :return: dict - extended route information.
    """
    return {**route, **more_route_information}


def fix_wagon_depot(wagons_rows):
    """Fix the list of rows of wagons.

    :param wagons_rows: list[list[tuple]] - the list of rows of wagons.
    :return: list[list[tuple]] - list of rows of wagons.
    """
    wagons_rows[0][1], wagons_rows[1][0] = wagons_rows[1][0], wagons_rows[0][1]
    wagons_rows[0][2], wagons_rows[2][0] = wagons_rows[2][0], wagons_rows[0][2]
    wagons_rows[1][2], wagons_rows[2][1] = wagons_rows[2][1], wagons_rows[1][2]
    return wagons_rows
