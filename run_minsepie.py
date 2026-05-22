#!/usr/bin/env python3
import argparse
import pandas as pd
import minsepie


#print(minsepie.__file__)
p = argparse.ArgumentParser()
p.add_argument("--in_csv", required=True)
p.add_argument("--out_csv", required=True)
p.add_argument("--onlyZ", default="False")
a = p.parse_args()

df = pd.read_csv(a.in_csv)
out = minsepie.predict(
    request=df,
    onlyZ=str(a.onlyZ).lower() in ("true", "t", "1")
)

if not isinstance(out, pd.DataFrame):
    out = pd.DataFrame(out)

out.to_csv(a.out_csv, index=False)
