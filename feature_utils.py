import os
import pandas as pd
import numpy as np

from pathlib import Path
from inspect import getsource

# Shooting
g_xg_ratio = lambda _df: _df.apply(lambda x: x["standard_gls"] / x["expected_xg"] if (x["expected_xg"] > 0) else 0, axis=1)

# Passing
cmp_pass_vs_team = lambda _df: _df['total_cmp%'] / (np.sum(_df['total_cmp%'] * _df['90s']) / np.sum(_df['90s']))
avg_pass_distance = lambda _df: _df.apply(lambda x: x["total_totdist"] / x["total_cmp"] if (x["total_cmp"] > 0) else np.nan, axis=1)
avg_pass_prg_distance = lambda _df: _df.apply(lambda x: x["total_prgdist"] / x["total_cmp"] if (x["total_cmp"] > 0) else np.nan, axis=1)
short_pass_cmp_pct = lambda _df: _df.apply(lambda x: x["short_cmp"] / x["total_cmp"] if (x["total_cmp"] > 0) else np.nan, axis=1)
medium_pass_cmp_pct = lambda _df: _df.apply(lambda x: x["medium_cmp"] / x["total_cmp"] if (x["total_cmp"] > 0) else np.nan, axis=1)
long_pass_cmp_pct = lambda _df: _df.apply(lambda x: x["long_cmp"] / x["total_cmp"] if (x["total_cmp"] > 0) else np.nan, axis=1)
key_pass_pct = lambda _df: _df.apply(lambda x: x["kp"] / x["total_cmp"] if (x["total_cmp"] > 0) else np.nan, axis=1)
third_pass_pct = lambda _df: _df.apply(lambda x: x["1/3"] / x["total_cmp"] if (x["total_cmp"] > 0) else np.nan, axis=1)
pen_pass_pct = lambda _df: _df.apply(lambda x: x["ppa"] / x["total_cmp"] if (x["total_cmp"] > 0) else np.nan, axis=1)
prg_pass_pct = lambda _df: _df.apply(lambda x: x["prgp"] / x["total_cmp"] if (x["total_cmp"] > 0) else np.nan, axis=1)
pen_cross_pct = lambda _df: _df.apply(lambda x: x["crspa"] / x["total_cmp"] if (x["total_cmp"] > 0) else np.nan, axis=1)

# Passing Types
live_pass_pct = lambda _df: _df.apply(lambda x: x["pass_types_live"] / x["total_cmp"] if (x["total_cmp"] > 0) else np.nan, axis=1)
dead_pass_pct = lambda _df: _df.apply(lambda x: x["pass_types_dead"] / x["total_cmp"] if (x["total_cmp"] > 0) else np.nan, axis=1)
through_pass_pct = lambda _df: _df.apply(lambda x: x["pass_types_tb"] / x["total_cmp"] if (x["total_cmp"] > 0) else np.nan, axis=1)
switch_pass_pct = lambda _df: _df.apply(lambda x: x["pass_types_sw"] / x["total_cmp"] if (x["total_cmp"] > 0) else np.nan, axis=1)
cross_pass_pct = lambda _df: _df.apply(lambda x: x["pass_types_crs"] / x["total_cmp"] if (x["total_cmp"] > 0) else np.nan, axis=1)
throwin_pass_pct = lambda _df: _df.apply(lambda x: x["pass_types_ti"] / x["total_cmp"] if (x["total_cmp"] > 0) else np.nan, axis=1)
blocked_pass_pct = lambda _df: _df.apply(lambda x: x["outcomes_blocks"] / x["total_cmp"] if (x["total_cmp"] > 0) else np.nan, axis=1)

# Goals and shot creation
sca_pass_pct = lambda _df: _df.apply(lambda x: x["sca_types_passlive"] / x["total_cmp"] if (x["total_cmp"] > 0) else np.nan, axis=1)
gca_pass_pct = lambda _df: _df.apply(lambda x: x["gca_types_passlive"] / x["total_cmp"] if (x["total_cmp"] > 0) else np.nan, axis=1)

# Defensive Actions
tackles_per_games_vs_team = lambda _df: _df.apply(lambda x: x["tackles_tkl"] / x["90s"] if (x["90s"] > 0) else np.nan, axis=1) / (_df['tackles_tkl'].sum() / 38 / 11) 
tackles_won_per_games_vs_team = lambda _df: _df.apply(lambda x: x["tackles_tklw"] / x["90s"] if (x["90s"] > 0) else np.nan, axis=1) / (_df['tackles_tklw'].sum() / 38 / 11) 
tackles_def3_per_games_vs_team = lambda _df: _df.apply(lambda x: x["tackles_def_3rd"] / x["90s"] if (x["90s"] > 0) else np.nan, axis=1) / (_df['tackles_def_3rd'].sum() / 38 / 11) 
tackles_mid3_per_games_vs_team = lambda _df: _df.apply(lambda x: x["tackles_mid_3rd"] / x["90s"] if (x["90s"] > 0) else np.nan, axis=1) / (_df['tackles_mid_3rd'].sum() / 38 / 11) 
tackles_att3_per_games_vs_team = lambda _df: _df.apply(lambda x: x["tackles_att_3rd"] / x["90s"] if (x["90s"] > 0) else np.nan, axis=1) / (_df['tackles_att_3rd'].sum() / 38 / 11) 
challenges_won_per_games_vs_team = lambda _df: _df.apply(lambda x: x["challenges_tkl"] / x["90s"] if (x["90s"] > 0) else np.nan, axis=1) / (_df['challenges_tkl'].sum() / 38 / 11) 
challenges_per_games_vs_team = lambda _df: _df.apply(lambda x: x["challenges_att"] / x["90s"] if (x["90s"] > 0) else np.nan, axis=1) / (_df['challenges_att'].sum() / 38 / 11) 
blocks_per_games_vs_team = lambda _df: _df.apply(lambda x: x["blocks_blocks"] / x["90s"] if (x["90s"] > 0) else np.nan, axis=1) / (_df['blocks_blocks'].sum() / 38 / 11) 
interceptions_per_games_vs_team = lambda _df: _df.apply(lambda x: x["int"] / x["90s"] if (x["90s"] > 0) else np.nan, axis=1) / (_df['int'].sum() / 38 / 11) 
clearences_per_games_vs_team = lambda _df: _df.apply(lambda x: x["clr"] / x["90s"] if (x["90s"] > 0) else np.nan, axis=1) / (_df['clr'].sum() / 38 / 11) 

# Possession
touches_per_game_vs_team = lambda _df: _df.apply(lambda x: x["touches_touches"] / x["90s"] if (x["90s"] > 0) else np.nan, axis=1) / (_df['touches_touches'].sum() / 38 / 11) 
touches_defpen_per_game_vs_team = lambda _df: _df.apply(lambda x: x["touches_def_pen"] / x["90s"] if (x["90s"] > 0) else np.nan, axis=1) / (_df['touches_def_pen'].sum() / 38 / 11) 
touches_def3_per_game_vs_team = lambda _df: _df.apply(lambda x: x["touches_def_3rd"] / x["90s"] if (x["90s"] > 0) else np.nan, axis=1) / (_df['touches_def_3rd'].sum() / 38 / 11) 
touches_mid3_per_game_vs_team = lambda _df: _df.apply(lambda x: x["touches_mid_3rd"] / x["90s"] if (x["90s"] > 0) else np.nan, axis=1) / (_df['touches_mid_3rd'].sum() / 38 / 11) 
touches_att3_per_game_vs_team = lambda _df: _df.apply(lambda x: x["touches_att_3rd"] / x["90s"] if (x["90s"] > 0) else np.nan, axis=1) / (_df['touches_att_3rd'].sum() / 38 / 11) 
touches_attpen_per_game_vs_team = lambda _df: _df.apply(lambda x: x["touches_att_pen"] / x["90s"] if (x["90s"] > 0) else np.nan, axis=1) / (_df['touches_att_pen'].sum() / 38 / 11) 
takeons_per_game_vs_team = lambda _df: _df.apply(lambda x: x["take-ons_att"] / x["90s"] if (x["90s"] > 0) else np.nan, axis=1) / (_df['take-ons_att'].sum() / 38 / 11) 
succ_takeons_vs_team = lambda _df: _df['take-ons_succ%'].fillna(0) / (np.sum(_df['take-ons_succ%'] * _df['90s']) / np.sum(_df['90s']))
carries_per_game_vs_team = lambda _df: _df.apply(lambda x: x["carries_carries"] / x["90s"] if (x["90s"] > 0) else np.nan, axis=1) / (_df['carries_carries'].sum() / 38 / 11) 
distance_per_carry = lambda _df: _df.apply(lambda x: x["carries_totdist"] / x["carries_carries"] if (x["carries_carries"] > 0) else np.nan, axis=1)
prg_distance_per_carry = lambda _df: _df.apply(lambda x: x["carries_prgdist"] / x["carries_carries"] if (x["carries_carries"] > 0) else np.nan, axis=1)
prg_distance_pct = lambda _df: _df.apply(lambda x: x["carries_prgdist"] / x["carries_totdist"] if (x["carries_totdist"] > 0) else np.nan, axis=1)
prg_carry_pct = lambda _df: _df.apply(lambda x: x["carries_prgc"] / x["carries_carries"] if (x["carries_carries"] > 0) else np.nan, axis=1)
carries3rd_per_carries = lambda _df: _df.apply(lambda x: x["carries_1/3"] / x["carries_carries"] if (x["carries_carries"] > 0) else np.nan, axis=1)
carries_pa_per_carries = lambda _df: _df.apply(lambda x: x["carries_cpa"] / x["carries_carries"] if (x["carries_carries"] > 0) else np.nan, axis=1)
receives_per_game_vs_team = lambda _df: _df.apply(lambda x: x["receiving_rec"] / x["90s"] if (x["90s"] > 0) else np.nan, axis=1) / (_df['receiving_rec'].sum() / 38 / 11) 
prgreceives_per_game_vs_team = lambda _df: _df.apply(lambda x: x["receiving_prgr"] / x["90s"] if (x["90s"] > 0) else np.nan, axis=1) / (_df['receiving_prgr'].sum() / 38 / 11) 

feature_functions = [g_xg_ratio, cmp_pass_vs_team, avg_pass_distance, avg_pass_prg_distance, short_pass_cmp_pct, medium_pass_cmp_pct, long_pass_cmp_pct, key_pass_pct, third_pass_pct, pen_pass_pct, prg_pass_pct, pen_cross_pct,
                     live_pass_pct, dead_pass_pct, through_pass_pct, switch_pass_pct, cross_pass_pct, throwin_pass_pct, blocked_pass_pct, sca_pass_pct, gca_pass_pct, tackles_per_games_vs_team, tackles_won_per_games_vs_team, tackles_def3_per_games_vs_team,
                     tackles_mid3_per_games_vs_team, tackles_att3_per_games_vs_team, challenges_won_per_games_vs_team, challenges_per_games_vs_team, blocks_per_games_vs_team, interceptions_per_games_vs_team, 
                     clearences_per_games_vs_team, touches_per_game_vs_team, touches_defpen_per_game_vs_team,
                     touches_def3_per_game_vs_team, touches_mid3_per_game_vs_team, touches_att3_per_game_vs_team, touches_attpen_per_game_vs_team, takeons_per_game_vs_team, succ_takeons_vs_team, carries_per_game_vs_team, distance_per_carry,
                     prg_distance_per_carry, prg_distance_pct, prg_carry_pct, carries3rd_per_carries, carries_pa_per_carries, receives_per_game_vs_team, prgreceives_per_game_vs_team]

INFO_COLUMNS = ['player', 'season', 'team', 'nation', 'pos', 'age', '90s']
SHOOTING_COLUMNS = ["standard_sot%", "standard_dist", "expected_npxg/sh"]
MISC_COLUMNS = ['aerial_duels_won%']

COLUMNS_TO_COLLECT = INFO_COLUMNS + SHOOTING_COLUMNS + MISC_COLUMNS
get_lambda_name = lambda l: getsource(l).split(' = ')[0]

def load_season_data(league, season, raw: bool = False):
    path = Path(os.path.abspath(__file__)).parent / 'data' / league / season
    file_list = os.listdir(path)

    # Loading the data from local folder
    data_dict = dict()
    for file_name in file_list:
        team_name = file_name.split(".")[0]
        team_data = pd.read_csv(path / file_name)
        team_data = team_data[~team_data["player"].isna()].iloc[:-2] # dropping aggregated stats
        team_data['team'] = team_name
        team_data['season'] = season
        data_dict[team_name] = team_data

    # For each team apply the feature calculation and concatenate the season
    team_dfs = []
    for _, team_data in data_dict.items():
        if not raw:
            created_features = [func(team_data).rename(get_lambda_name(func)) for func in feature_functions]
            team_df = pd.concat(created_features, axis=1)
            team_df = pd.concat([team_data[COLUMNS_TO_COLLECT].fillna(0), team_df], axis=1)
        else:
            team_df = team_data
        team_dfs.append(team_df)
    df = pd.concat(team_dfs, axis=0)
    df.set_index('player', inplace=True)

    return df