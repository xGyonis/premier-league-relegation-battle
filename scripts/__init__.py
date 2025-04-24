import os
import pandas as pd

RAW_DIR = "data/raw"
PROCESSED_DIR = "data/processed"

# Create processed folder if not exist
os.makedirs(PROCESSED_DIR, exist_ok=True)

def clean_season(file_path):
    try:
        df = pd.read_csv(file_path)

        # Basic columns to keep (common across seasons)
        cols_to_keep = ['Date', 'HomeTeam', 'AwayTeam', 'FTHG', 'FTAG', 'FTR']
        df = df[[col for col in cols_to_keep if col in df.columns]]

        # Rename columns for consistency
        df.columns = ['date', 'home_team', 'away_team', 'home_goals', 'away_goals', 'result']

        # Standardize date format (try multiple formats)
        df['date'] = pd.to_datetime(df['date'], errors='coerce', dayfirst=True)

        # Drop rows with missing dates
        df.dropna(subset=['date'], inplace=True)

        return df
    except Exception as e:
        print(f"❌ Failed to clean {file_path}: {e}")
        return None

def main():
    for filename in os.listdir(RAW_DIR):
        if filename.endswith(".csv"):
            raw_path = os.path.join(RAW_DIR, filename)
            processed_path = os.path.join(PROCESSED_DIR, filename)

            df_cleaned = clean_season(raw_path)

            if df_cleaned is not None:
                df_cleaned.to_csv(processed_path, index=False)
                print(f"✅ Cleaned & saved: {processed_path}")

if __name__ == "__main__":
    main()
