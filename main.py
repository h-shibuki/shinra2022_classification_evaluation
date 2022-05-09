import argparse

from data_utils import DataUtils
from score_utils import scoring


def load_arg():
    parser = argparse.ArgumentParser(description="Scoring SHINRA-ML result.")
    parser.add_argument("submission_path", type=str, help="Path to submission result file.")
    parser.add_argument("answer_path", type=str, help="Path to answer file.")
    parser.add_argument("--use_patch", default=True, help="If use patch of SHINRA2021-ml, store True.")
    args = parser.parse_args()
    return args


def main():
    args = load_arg()

    # ワンライナーJsonの読み込み
    submission_results = DataUtils.JsonL.load(args.submission_path)
    answer = DataUtils.JsonL.load(args.answer_path)

    # 評価
    score = scoring(submission_results, answer)
    print(score)


if __name__ == "__main__":
    main()
