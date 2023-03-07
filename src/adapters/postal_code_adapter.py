import pgeocode
from numpy import NAN


def get_locality_by_cp(cp: str) -> str:
    """Retorna la localitat donat un codi postal

    :param cp:
    :return:
    """
    nomi = pgeocode.Nominatim("es")
    locality = nomi.query_postal_code(codes=cp)["community_name"]
    return locality if locality is not NAN else ""


if __name__ == "__main__":
    nomi = pgeocode.Nominatim("es")
    res = nomi.query_postal_code("08014")
    print(res)
