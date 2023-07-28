import pandas as pd


class TsvUse():
    def __int__(self):
            pass

    def write_tsv(self, path_tsv, data_dict):



        data = {"id": all_id,
                "text": all_text,
                "title": all_title, }
        df = pd.DataFrame(data)
        df.to_csv(path_tsv, sep="\t", index=False)