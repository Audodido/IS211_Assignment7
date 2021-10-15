import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--players", help="Number of players", type=str, required=False)
args = parser.parse_args()

print(f"Players {args.players}")