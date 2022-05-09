from collections import defaultdict


def calc_f1(cnt):
    if not cnt["TP"]:
        return 0.0, 0.0, 0.0
    precision = cnt["TP"] / cnt["TPFP"]
    recall = cnt["TP"] / cnt["TPFN"]
    f1 = 2 * precision * recall / (precision + recall)
    return {"Precision": precision * 100, "Recall": recall * 100, "F1": f1 * 100}


def correct_ene(enes):
    corrected_enes = set()
    flag_Living_Thing: bool = False
    for ene in enes:
        # 森羅2022では例外的なカテゴリはないのでコメントアウト
        # if ene == "1.5.1.1" or ene == "1.5.1.2":  # 市区町村名と都道府県郡州名を結合
        #     ene = "1.5.1.12"
        # if ene[:6] == "1.10.4":  # 1.10.4(生物名)以下は除外するフラグを立てる
        #     flag_Living_Thing = True
        corrected_enes.add(ene)
    return corrected_enes, flag_Living_Thing


def scoring(results, answers, use_patch=True, level=None):
    ext_ene_ids = lambda x: set(str(_x["ENE_id"]).strip() for _x in x)

    answers = {str(d["pageid"]): ext_ene_ids(d["ENEs"]) for d in answers}
    results = {str(d["pageid"]): ext_ene_ids(d["ENEs"]) for d in results}

    cnt = defaultdict(int)
    for pageid, answer_enes in answers.items():
        result_enes = results.get(str(pageid), {"9"})  # 提出結果が欠けている場合はIGNOREDを格納

        if use_patch:  # SHINRA2021-MLの評価用パッチの使用
            answer_enes, flag_Living_Thing = correct_ene(answer_enes)
            result_enes, _ = correct_ene(result_enes)
            if flag_Living_Thing:  # 1.10.4(生物名)以下は除外
                continue

        cnt["TP"] += len(answer_enes & result_enes)
        cnt["TPFP"] += len(result_enes)
        cnt["TPFN"] += len(answer_enes)
    return calc_f1(cnt)
