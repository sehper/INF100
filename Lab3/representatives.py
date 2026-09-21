import requests


def main():
    data = download_data()
    representatives = data['dagensrepresentanter_liste']

    people_of_interest = []
    for person in representatives:
        if person['fylke']['navn'] == 'Hordaland':
            people_of_interest.append(person)

    people_of_interest.sort(key=get_last_name_lowercase)

    for person in people_of_interest:
        full_name = f"{person['fornavn']} {person['etternavn']}"
        party = person['parti']['id']
        print(f"{full_name} ({party})")


def download_data():
    url = "https://data.stortinget.no/eksport/dagensrepresentanter?format=json"
    response = requests.get(url, headers={"User-Agent": "no.uib.ii.inf100"})
    data = response.json()
    return data


def get_last_name_lowercase(person):
    return person['etternavn'].lower()


if __name__ == '__main__':
    main()