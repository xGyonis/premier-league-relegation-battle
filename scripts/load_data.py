import os
import requests

def build_season_code(start_year):
    """
    Converts a season like 2000 to a code like '0001' for football-data.co.uk
    """
    end_year = (start_year + 1) % 100
    return f"{str(start_year % 100).zfill(2)}{str(end_year).zfill(2)}"

def download_csv(url, save_path):
    try:
        response = requests.get(url)
        response.raise_for_status() 
        with open(save_path, 'wb') as f:
            f.write(response.content)
        print(f"✅ Downloaded: {save_path}")
    except requests.exceptions.RequestException:
        print(f"❌ Failed to download: {url}")

def main():
    os.makedirs("data/raw", exist_ok=True)

    for year in range(2000, 2025):
        season_code = build_season_code(year)
        url = f"https://www.football-data.co.uk/mmz4281/{season_code}/E0.csv"
        filename = f"data/raw/{year}-{str(year+1)[-2:]}.csv"
        download_csv(url, filename)

if __name__ == "__main__":
    main()
