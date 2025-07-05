def display_comparison_table(comparison_df):
    comparison_df = comparison_df.fillna(0)
    print("\n" + "=" * 80)
    print("\U0001F3C6 MID LANER COMPARISION")
    print("=" * 80)
    print(comparison_df.to_string(float_format='%.2f'))

    print("\n\U0001F4CA PERFORMANCE OVERVIEW:")
    print("-" * 50)
    numeric_df = comparison_df.select_dtypes(include=['float64', 'int64'])
    if not numeric_df.empty:
        for column in numeric_df.columns:
            valid_data = numeric_df[column].dropna()
            if len(valid_data) > 0:
                best_player = valid_data.idxmax()
                best_value = valid_data.max()
                print(f"🥇 {column}: {best_player} ({best_value:.3f})")

        print("💥💥💥 CHOVY DOMINATES EVERY TOP OPPONENT💥💥💥")
        print("👑👑👑 WHEN CONSISTENCY MEETS MECHANICAL PERFECTION, YOU GET THE BEST MID LANER IN THE WORLD👑👑👑")
    print("=" * 80)