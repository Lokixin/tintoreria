import pgeocode
from numpy import NAN


def get_locality_by_cp(cp: str) -> str:
    nomi = pgeocode.Nominatim("es")
    locality = nomi.query_postal_code(codes=cp)["community_name"]
    return locality if locality is not NAN else ""


if __name__ == "__main__":
    nomi = pgeocode.Nominatim("es")
    res = nomi.query_postal_code("sadasd")
    print(res["community_name"] is NAN)
