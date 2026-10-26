def main():
    list_years =  [
        1900,
        1800,
        2000,
        1500,
    ]

    for year in list_years:
        print(f"year: {year}, century: {grouped_year(year)}")


def grouped_year(year):
    return f"{(year // 100) + 1}th century"


if __name__ == "__main__":
    main()