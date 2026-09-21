"""Estimate a video job's cost from the per-second rates listed on piapi.ai.

These are the 'from' figures shown on the home page snapshot used for this repo.
They are the lowest tier for each model and change; https://piapi.ai/pricing wins.
"""
import sys

PER_SECOND_USD = {
    'seedance-2.5': 0.15,
    'seedance-2.0': 0.042,
    'kling-3.0': 0.10,
    'veo-3.1': 0.06,
    'wan-2.6': 0.08,
    'minimax-h3': 0.03,
    'framepack': 0.03,
}


def estimate(model: str, seconds: float, clips: int = 1) -> float:
    rate = PER_SECOND_USD[model]
    return rate * seconds * clips


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('usage: cost_estimate.py MODEL SECONDS [CLIPS]')
        print('models:', ', '.join(sorted(PER_SECOND_USD)))
        sys.exit(1)
    model = sys.argv[1]
    seconds = float(sys.argv[2])
    clips = int(sys.argv[3]) if len(sys.argv) > 3 else 1
    total = estimate(model, seconds, clips)
    print(f'{clips} x {seconds:g}s on {model}: about ${total:.2f} at the listed from-rate')
    print('New accounts get $0.50 free credit; compare before running a batch.')
